const assert = require('node:assert/strict')
const { spawnSync } = require('node:child_process')
const fs = require('node:fs')
const os = require('node:os')
const path = require('node:path')
const { test } = require('node:test')

const cli = path.resolve(__dirname, '../../tools/clis/meta-ads.js')
function run(argv, env, response = "throw new Error('unexpected network request')") {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'marketing-cli-'))
  const mock = path.join(tmp, 'fetch.cjs')
  fs.writeFileSync(mock, `const assert = require('node:assert/strict'); global.fetch = async (url, opts) => { ${response} };`)
  const childEnv = { ...process.env, ...env }
  for (const [key, value] of Object.entries(env)) if (value === undefined) delete childEnv[key]
  try {
    return spawnSync(process.execPath, ['--require', mock, cli, ...argv], { env: childEnv, encoding: 'utf8', timeout: 10000 })
  } finally {
    fs.rmSync(tmp, { recursive: true, force: true })
  }
}
function value(result) {
  assert.equal(result.status, 0, result.stderr)
  return JSON.parse(result.stdout)
}

for(const accountId of ['12345','act_12345']) {
  for(const source of ['argument','environment']) {
    test(`ad account ${accountId} from ${source} has exactly one act_ prefix`,()=>{
      const argv=['campaigns','list']; const env={META_ACCESS_TOKEN:'fixture-token',META_AD_ACCOUNT_ID:undefined}
      if(source==='argument')argv.push('--account-id',accountId); else env.META_AD_ACCOUNT_ID=accountId
      const result=run(argv,env,`assert.equal(new URL(url).pathname,'/v18.0/act_12345/campaigns');
        return new Response(JSON.stringify({data:[{id:'campaign42'}]}));`)
      assert.equal(value(result).data[0].id,'campaign42')
    })
  }
}
test('audience creation accepts the canonical account ID returned by accounts list',()=>{
  const result=run(['audiences','create-lookalike','--account-id','act_12345','--source-id','source42','--country','US'],{META_ACCESS_TOKEN:'fixture-token'},`
    assert.equal(new URL(url).pathname,'/v18.0/act_12345/customaudiences');
    assert.equal(opts.method,'POST'); assert.equal(JSON.parse(opts.body).origin_audience_id,'source42');
    return new Response(JSON.stringify({id:'audience42'}));`)
  assert.equal(value(result).id,'audience42')
})
test('dry-run preserves the corrected account route and masks the token',()=>{
  const result=run(['adsets','list','--account-id','act_12345','--dry-run'],{META_ACCESS_TOKEN:'fixture-token'})
  assert.equal(new URL(value(result).url).pathname,'/v18.0/act_12345/adsets')
  assert.equal(result.stdout.includes('fixture-token'),false)
})
