const { test } = require('node:test')
const assert = require('node:assert/strict')
const { spawnSync } = require('node:child_process')
const path = require('node:path')
const cli = path.resolve(__dirname, '../../tools/clis/outreach.js')
function run(args, oracle = '', env = {}) {
  const code = `global.fetch = async (url, options) => {
    const assert = require('node:assert/strict');
    const parsed = new URL(url);
    const body = options.body ? JSON.parse(options.body) : null;
    ${oracle}
    return new Response(JSON.stringify({accepted:true, url, body}), {status:200});
  }; process.argv = ['node', ${JSON.stringify(cli)}, ...${JSON.stringify(args)}]; require(${JSON.stringify(cli)});`
  const childEnv = {...process.env, OUTREACH_ACCESS_TOKEN:'test-token', ...env}
  for (const [key, value] of Object.entries(childEnv)) if (value === undefined) delete childEnv[key]
  const r = spawnSync(process.execPath, ['-e', code], {encoding:'utf8', env:childEnv, timeout:10000})
  return r
}
function result(r) { assert.equal(r.status,0,r.stderr); return JSON.parse(r.stdout) }
test('documented incomplete task filter reaches the vendor state field', () => {
  const p = result(run(['tasks','list','--status','incomplete'], "assert.equal(parsed.searchParams.get('filter[state]'), 'incomplete'); assert.equal(parsed.searchParams.has('filter[status]'), false);"))
  assert.equal(p.accepted,true)
})
test('new state spelling works for completed tasks', () => {
  assert.equal(result(run(['tasks','list','--state','complete'], "assert.equal(parsed.searchParams.get('filter[state]'), 'complete');")).accepted,true)
})
test('unfiltered list still requests all task states', () => {
  assert.equal(result(run(['tasks','list'], "assert.equal(parsed.search, '');")).accepted,true)
})
test('filtered preview never sends a request or exposes credentials', () => {
  const p = result(run(['tasks','list','--status','pending','--dry-run'], "throw new Error('unexpected fetch')"))
  assert.equal(new URL(p.url).searchParams.get('filter[state]'),'pending'); assert.equal(p.headers.Authorization,'Bearer ***')
})
