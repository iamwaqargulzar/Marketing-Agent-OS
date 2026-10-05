const { test } = require('node:test')
const assert = require('node:assert/strict')
const { spawnSync } = require('node:child_process')
const path = require('node:path')
const cli = path.resolve(__dirname, '../../tools/clis/onesignal.js')
function run(args, network = false) {
  const code = `global.fetch = async (url, options) => {
    if (!${network}) throw new Error('Unexpected network request');
    if (!url.startsWith('https://api.onesignal.com/apps/app123/users')) throw new Error('Unknown user route');
    const body = options.body ? JSON.parse(options.body) : null;
    if (body && body.tags) throw new Error('Tags must be nested in properties');
    return { status: 200, text: async () => JSON.stringify({url, method: options.method, body}) };
  }; process.argv = ['node', ${JSON.stringify(cli)}, ...${JSON.stringify(args)}]; require(${JSON.stringify(cli)});`
  return spawnSync(process.execPath, ['-e', code], {encoding: 'utf8', env: {...process.env, ONESIGNAL_REST_API_KEY: 'test-only-key', ONESIGNAL_APP_ID: 'app123'}})
}
test('create user reaches the User Model route and preserves segment tags', () => {
  const r = run(['users', 'create', '--external-id', 'customer', '--tags', '{"plan":"pro"}'], true)
  assert.equal(r.status, 0, r.stderr)
  const response = JSON.parse(r.stdout)
  assert.deepEqual(response.body.identity, { external_id: 'customer' })
  assert.deepEqual(response.body.properties, { tags: { plan: 'pro' } })
})
for (const sub of ['get', 'delete']) test(`${sub} encodes complete alias ID as one path segment`, () => {
  const r = run(['users', sub, '--alias-id', 'tenant/customer+test@example.com', '--dry-run'])
  assert.equal(r.status, 0, r.stderr)
  assert.equal(JSON.parse(r.stdout).url, 'https://api.onesignal.com/apps/app123/users/by/external_id/tenant%2Fcustomer%2Btest%40example.com')
})
test('create preview masks authorization and uses the same schema', () => {
  const r = run(['users', 'create', '--external-id', 'customer', '--tags', '{"plan":"pro"}', '--dry-run'])
  const body = JSON.parse(r.stdout)
  assert.equal(body.headers.Authorization, '***')
  assert.deepEqual(body.body.properties.tags, {plan: 'pro'})
})
test('invalid tags and missing identity fail locally', () => {
  for (const args of [['users', 'create', '--external-id', 'customer', '--tags', '[]'], ['users', 'create', '--tags', '{}']]) {
    const r = run(args)
    assert.ok(JSON.parse(r.stdout).error)
  }
})
