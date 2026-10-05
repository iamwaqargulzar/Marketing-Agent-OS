const { test } = require('node:test')
const assert = require('node:assert/strict')
const { spawnSync } = require('node:child_process')
const path = require('node:path')
const cli = path.resolve(__dirname, '../../tools/clis/google-ads.js')
function run(args, oracle = '', env = {}) {
  const code = `global.fetch = async (url, options) => {
    const assert = require('node:assert/strict');
    const parsed = new URL(url);
    const body = options.body ? JSON.parse(options.body) : null;
    ${oracle}
    return new Response(JSON.stringify({accepted:true, url, body}), {status:200});
  }; process.argv = ['node', ${JSON.stringify(cli)}, ...${JSON.stringify(args)}]; require(${JSON.stringify(cli)});`
  const childEnv = {...process.env, GOOGLE_ADS_TOKEN:'test-token', GOOGLE_ADS_DEVELOPER_TOKEN:'test-developer', GOOGLE_ADS_CUSTOMER_ID:'5556667777', ...env}
  for (const [key, value] of Object.entries(childEnv)) if (value === undefined) delete childEnv[key]
  const r = spawnSync(process.execPath, ['-e', code], {encoding:'utf8', env:childEnv, timeout:10000})
  return r
}
function result(r) { assert.equal(r.status,0,r.stderr); return JSON.parse(r.stdout) }
for (const args of [['campaigns','list'],['campaigns','pause','--id','42']]) test(`${args[1]} forwards manager access context`, () => {
  const p = result(run(args, "assert.equal(options.headers['login-customer-id'], '1234567890'); assert.ok(parsed.pathname.startsWith('/v24/customers/5556667777/'));", {GOOGLE_ADS_LOGIN_CUSTOMER_ID:'123-456-7890'}))
  assert.equal(p.accepted,true)
})
test('direct account request does not gain an unnecessary manager header', () => {
  assert.equal(result(run(['account','info'], "assert.equal(options.headers['login-customer-id'], undefined);", {GOOGLE_ADS_LOGIN_CUSTOMER_ID:undefined})).accepted,true)
})
test('manager preview includes normalized header and masks credentials', () => {
  const p = result(run(['campaigns','list','--dry-run'], "throw new Error('unexpected fetch')", {GOOGLE_ADS_LOGIN_CUSTOMER_ID:'123-456-7890'}))
  assert.equal(p.headers['login-customer-id'],'1234567890'); assert.equal(p.headers.Authorization,'***'); assert.equal(p.headers['developer-token'],'***')
})
