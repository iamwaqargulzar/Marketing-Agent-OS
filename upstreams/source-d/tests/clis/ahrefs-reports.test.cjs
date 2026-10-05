const {test} = require('node:test')
const assert = require('node:assert/strict')
const {spawnSync} = require('node:child_process')
const path = require('node:path')
const cli = path.resolve(__dirname, '../../tools/clis/ahrefs.js')
function run(args, oracle='') {
  const code = `global.fetch = async (url, options) => {
    const assert = require('node:assert/strict'); const parsed = new URL(url);
    const body = options.body ? JSON.parse(options.body) : null;
    ${oracle}
    return new Response(JSON.stringify({accepted:true,url,body}), {status:200});
  }; process.argv = ['node',${JSON.stringify(cli)},...${JSON.stringify(args)}]; require(${JSON.stringify(cli)});`
  return spawnSync(process.execPath,['-e',code], {encoding:'utf8',timeout:10000,env:{...process.env, AHREFS_API_KEY:'test-only-key'}})
}
function output(r) { assert.equal(r.status,0,r.stderr); return JSON.parse(r.stdout) }
function localError(r, pattern) { const text = r.status === 0 ? r.stdout : r.stderr; assert.match(JSON.parse(text).error,pattern) }
const commands = [['domain-rating','get'], ['keywords','organic'], ['top-pages','list']]
for (const command of commands) test(`${command[0]} forwards an explicit report date and chosen columns`, () => {
  const args = [...command,'--target','example.com','--date','2024-02-29','--select','keyword,url','--country','us','--limit','10']
  const oracle = "assert.equal(parsed.searchParams.get('date'),'2024-02-29');" + (command[0] === 'domain-rating' ? "assert.equal(parsed.searchParams.has('select'),false);" : "assert.equal(parsed.searchParams.get('select'),'keyword,url'); assert.equal(parsed.searchParams.get('country'),'us'); assert.equal(parsed.searchParams.get('limit'),'10');")
  assert.equal(output(run(args, oracle)).accepted,true)
})
for (const command of commands) test(`${command[0]} defaults a missing report date to today (UTC)`, () => {
  const oracle = "assert.match(parsed.searchParams.get('date'), /^\\d{4}-\\d{2}-\\d{2}$/); assert.equal(parsed.searchParams.get('date'), new Date().toISOString().slice(0, 10));"
  assert.equal(output(run([...command,'--target','example.com','--select','url'], oracle)).accepted,true)
})
test('invalid calendar dates and date flag without a value are rejected', () => {
  for (const date of ['2023-02-29','2026-04-31','2026-13-01','2026-1-01','not-a-date']) localError(run(['domain-rating','get','--target','example.com','--date',date], "throw new Error('unexpected paid request')"),/date/)
  localError(run(['domain-rating','get','--target','example.com','--date'], "throw new Error('unexpected paid request')"),/date/)
})
for (const command of commands.slice(1)) test(`${command[0]} rejects empty selected fields and defaults when omitted`, () => {
  for (const suffix of [['--select'],['--select',''],['--select',' , ']]) localError(run([...command,'--target','example.com','--date','2026-09-30',...suffix], "throw new Error('unexpected paid request')"),/select/)
  assert.equal(output(run([...command,'--target','example.com','--date','2026-09-30'], "assert.ok(parsed.searchParams.get('select').split(',').length >= 3)")).accepted,true)
})
test('domain rating does not require selected fields', () => {
  assert.equal(output(run(['domain-rating','get','--target','example.com','--date','2026-09-30'], "assert.equal(parsed.searchParams.get('date'),'2026-09-30');")).accepted,true)
})
test('other commands retain their existing request inputs', () => {
  const p=output(run(['backlinks','list','--target','example.com','--limit','5'], "assert.equal(parsed.searchParams.has('date'),false); assert.equal(parsed.searchParams.get('limit'),'5');")); assert.equal(p.accepted,true)
})
test('dated report preview is complete and masks authorization', () => {
  const p=output(run(['top-pages','list','--target','example.com','--date','2026-09-30','--select','url','--dry-run'], "throw new Error('unexpected paid request')")); assert.equal(new URL(p.url).searchParams.get('select'),'url'); assert.equal(p.headers.Authorization,'***')
})
