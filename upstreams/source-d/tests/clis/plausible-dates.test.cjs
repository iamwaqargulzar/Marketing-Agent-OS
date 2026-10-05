const {test} = require('node:test')
const assert = require('node:assert/strict')
const {spawnSync} = require('node:child_process')
const path = require('node:path')
const cli = path.resolve(__dirname, '../../tools/clis/plausible.js')
function run(args, oracle='') {
  const code = `global.fetch = async (url, options) => {
    const assert = require('node:assert/strict'); const parsed = new URL(url);
    const body = options.body ? JSON.parse(options.body) : null;
    ${oracle}
    return new Response(JSON.stringify({accepted:true,url,body}), {status:200});
  }; process.argv = ['node',${JSON.stringify(cli)},...${JSON.stringify(args)}]; require(${JSON.stringify(cli)});`
  return spawnSync(process.execPath,['-e',code], {encoding:'utf8',timeout:10000,env:{...process.env, PLAUSIBLE_API_KEY:'test-only-key'}})
}
function output(r) { assert.equal(r.status,0,r.stderr); return JSON.parse(r.stdout) }
function localError(r, pattern) { const text = r.status === 0 ? r.stdout : r.stderr; assert.match(JSON.parse(text).error,pattern) }
for (const sub of ['aggregate','timeseries','pages','sources','countries','devices','utm','query']) test(`${sub} sends a custom range as a JSON array`, () => {
  const range=['2026-09-01','2026-09-30']
  const p=output(run(['stats',sub,'--site-id','example.com','--metrics','visitors','--date-range',JSON.stringify(range)], "assert.deepEqual(body.date_range,['2026-09-01','2026-09-30']); assert.equal(options.method,'POST');")); assert.equal(p.accepted,true)
})
test('custom timestamp offsets are preserved exactly', () => {
  const range=['2026-09-01T12:00:00+02:00','2026-09-01T15:59:59+02:00']
  const p=output(run(['stats','aggregate','--site-id','example.com','--date-range',JSON.stringify(range)])); assert.deepEqual(p.body.date_range,range)
})
test('malformed arrays and non-string boundaries are rejected before HTTP', () => {
  for (const range of ['[bad','[]','["2026-09-01"]','["a","b","c"]','[1,"2026-09-30"]','["","2026-09-30"]']) localError(run(['stats','aggregate','--site-id','example.com','--date-range',range], "throw new Error('unexpected query')"),/date-range/)
})
test('presets and the default retain their original request type', () => {
  assert.equal(output(run(['stats','aggregate','--site-id','example.com','--date-range','7d'])).body.date_range,'7d')
  assert.equal(output(run(['stats','aggregate','--site-id','example.com'])).body.date_range,'30d')
})
test('unrelated site routes are not gated by statistics range parsing', () => {
  const p=output(run(['sites','list','--date-range','[bad'], "assert.equal(parsed.pathname,'/api/v1/sites'); assert.equal(options.method,'GET');")); assert.equal(p.accepted,true)
})
test('realtime visitor route is not gated by a range it does not use', () => {
  const p=output(run(['stats','realtime','--site-id','example.com','--date-range','[bad'], "assert.equal(parsed.pathname,'/api/v1/stats/realtime/visitors');")); assert.equal(p.accepted,true)
})
test('custom range preview shows its array and masks authorization', () => {
  const p=output(run(['stats','aggregate','--site-id','example.com','--date-range','["2026-09-01","2026-09-30"]','--dry-run'], "throw new Error('unexpected query')")); assert.deepEqual(p.body.date_range,['2026-09-01','2026-09-30']); assert.equal(p.headers.Authorization,'***')
})
