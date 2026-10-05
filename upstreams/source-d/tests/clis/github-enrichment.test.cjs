const { test } = require('node:test')
const assert = require('node:assert/strict')
const { spawnSync } = require('node:child_process')
const path = require('node:path')

const cli = path.resolve(__dirname, '../../tools/clis/github-prospects.js')
function run(command, status, args = []) {
  const source = `global.fetch = async url => {
    const profile = String(url).includes('/users/');
    const status = profile ? ${status} : 200;
    return {status, ok: status === 200, headers: {get: () => null},
      text: async () => JSON.stringify({message:'fixture failure'}),
      json: async () => profile ? {login:'alice',email:null,company:'Example',type:'User'} : ${JSON.stringify(command === 'forks' ? [{owner:{login:'alice'}}] : [{login:'alice'}])}};
  }; process.argv = ['node', ${JSON.stringify(cli)}, ${JSON.stringify(command)}, 'owner/repo', '--enrich', ...${JSON.stringify(args)}]; require(${JSON.stringify(cli)});`
  return spawnSync(process.execPath, ['-e', source], {encoding:'utf8', env:{...process.env,GITHUB_TOKEN:'fixture-key'}})
}
test('authentication or rate-limit failures cannot look like a successful empty prospect export', () => {
  for (const command of ['stargazers','forks','watchers']) {
    for (const status of [401,403,429,500]) {
      const result = run(command, status, ['--format','csv'])
      assert.equal(result.status, 1, `${command}/${status}: ${result.stdout}`)
      assert.equal(result.stdout, '')
      assert.match(JSON.parse(result.stderr).error, new RegExp(`Profile enrichment failed: HTTP ${status}`))
    }
  }
})
test('deleted profiles can still be skipped', () => {
  const result = run('stargazers',404)
  assert.equal(result.status,0,result.stderr)
  assert.equal(JSON.parse(result.stdout).count,0)
})
test('normal profiles and legitimate filter non-matches still return success', () => {
  const success = run('stargazers',200)
  assert.equal(success.status,0,success.stderr)
  assert.equal(JSON.parse(success.stdout).users[0].login,'alice')
  const filtered = run('watchers',200,['--with-email'])
  assert.equal(filtered.status,0,filtered.stderr)
  assert.equal(JSON.parse(filtered.stdout).count,0)
})
