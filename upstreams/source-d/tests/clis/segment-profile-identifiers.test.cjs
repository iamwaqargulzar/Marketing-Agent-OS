const { test } = require('node:test')
const assert = require('node:assert/strict')
const { spawnSync } = require('node:child_process')
const path = require('node:path')
const cli = path.resolve(__dirname, '../../tools/clis/segment.js')
function run(args, oracle = '', env = {}) {
  const code = `global.fetch = async (url, options) => {
    const assert = require('node:assert/strict');
    const parsed = new URL(url);
    const body = options.body ? JSON.parse(options.body) : null;
    ${oracle}
    return new Response(JSON.stringify({accepted:true, url, body}), {status:200});
  }; process.argv = ['node', ${JSON.stringify(cli)}, ...${JSON.stringify(args)}]; require(${JSON.stringify(cli)});`
  const childEnv = {...process.env, SEGMENT_WRITE_KEY:'test-write', SEGMENT_ACCESS_TOKEN:'test-access', ...env}
  for (const [key, value] of Object.entries(childEnv)) if (value === undefined) delete childEnv[key]
  const r = spawnSync(process.execPath, ['-e', code], {encoding:'utf8', env:childEnv, timeout:10000})
  return r
}
function result(r) { assert.equal(r.status,0,r.stderr); return JSON.parse(r.stdout) }
for (const sub of ['traits','events']) test(`profile ${sub} preserves complete special-character user ID`, () => {
  const id = 'tenant/customer+test@example.com?#details'
  const r = run(['profiles',sub,'--space-id','space123','--user-id',id], `assert.equal(parsed.search, ''); assert.equal(parsed.hash, ''); assert.equal(decodeURIComponent(parsed.pathname.split('/')[7]), 'user_id:' + ${JSON.stringify(id)}); assert.equal(parsed.pathname.split('/')[8], ${JSON.stringify(sub)});`)
  assert.equal(result(r).accepted,true)
})
test('simple profile identifier remains routable', () => {
  assert.equal(result(run(['profiles','traits','--space-id','space123','--user-id','user123'], "assert.equal(parsed.pathname, '/v1/spaces/space123/collections/users/profiles/user_id:user123/traits');")).accepted,true)
})
test('tracking event payload is unchanged', () => {
  assert.deepEqual(result(run(['track','event','--user-id','tenant/customer','--event','Signup'], "assert.equal(parsed.pathname, '/v1/track');")).body, {userId:'tenant/customer',event:'Signup'})
})
test('profile dry-run uses the encoded path without leaking authorization', () => {
  const r = run(['profiles','events','--space-id','space123','--user-id','a/b?c','--dry-run'], "throw new Error('unexpected fetch')")
  const p = result(r); assert.equal(p.url,'https://profiles.segment.com/v1/spaces/space123/collections/users/profiles/user_id:a%2Fb%3Fc/events'); assert.equal(p.headers.Authorization,'***')
})
