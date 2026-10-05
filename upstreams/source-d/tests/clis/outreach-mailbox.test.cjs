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
test('email sequence enrollment carries the selected sending mailbox', () => {
  const p = result(run(['sequence-states','create','--sequence-id','7','--prospect-id','42','--mailbox-id','9'], "assert.equal(parsed.pathname, '/api/v2/sequenceStates'); assert.deepEqual(body.data.relationships.mailbox, {data:{type:'mailbox', id:'9'}});"))
  assert.equal(p.accepted,true); assert.deepEqual(p.body.data.relationships.prospect,{data:{type:'prospect',id:'42'}})
})
test('mailbox relationship is visible in a redacted preview', () => {
  const p = result(run(['sequence-states','create','--sequence-id','7','--prospect-id','42','--mailbox-id','9','--dry-run'], "throw new Error('unexpected fetch')"))
  assert.deepEqual(p.body.data.relationships.mailbox,{data:{type:'mailbox',id:'9'}}); assert.equal(p.headers.Authorization,'Bearer ***')
})
test('call-only sequence can retain an omitted mailbox', () => {
  const p = result(run(['sequence-states','create','--sequence-id','7','--prospect-id','42'], "assert.equal(body.data.relationships.mailbox, undefined);"))
  assert.equal(p.accepted,true)
})
test('prospect creation is unaffected by the sequence mailbox option', () => {
  const p = result(run(['prospects','create','--email','customer@example.com'], "assert.equal(parsed.pathname, '/api/v2/prospects');"))
  assert.deepEqual(p.body.data.attributes.emails,['customer@example.com'])
})
