const assert = require('node:assert/strict')
const { spawnSync } = require('node:child_process')
const fs = require('node:fs')
const os = require('node:os')
const path = require('node:path')
const { test } = require('node:test')

const cli = path.resolve(__dirname, '../../tools/clis/ga4.js')
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

const mpArgs=['events','send','--measurement-id','G-FIXTURE','--api-secret','fixture-secret','--client-id','123.456','--event-name','purchase']
test('Measurement Protocol works with its API secret and no OAuth token', () => {
  const result=run(mpArgs,{GA4_ACCESS_TOKEN:undefined},`
    const query=new URL(url).searchParams; assert.equal(query.get('api_secret'),'fixture-secret');
    assert.equal(opts.headers.Authorization,undefined); assert.equal(opts.method,'POST');
    assert.equal(JSON.parse(opts.body).events[0].name,'purchase');
    return new Response(null,{status:204});`)
  assert.deepEqual(value(result),{status:204,success:true})
})
test('Measurement Protocol dry-run needs no unrelated OAuth token and masks secret', () => {
  const result=run([...mpArgs,'--dry-run'],{GA4_ACCESS_TOKEN:undefined})
  assert.equal(value(result)._dry_run,true)
  assert.equal(new URL(value(result).url).searchParams.get('api_secret'),'***')
  assert.equal(result.stdout.includes('fixture-secret'),false)
})
test('report commands still reject absent OAuth before any request', () => {
  const result=run(['reports','run','--property','123'],{GA4_ACCESS_TOKEN:undefined})
  assert.equal(result.status,1)
  assert.match(result.stderr,/GA4_ACCESS_TOKEN/)
})
test('report commands continue using OAuth when configured', () => {
  const result=run(['reports','run','--property','123'],{GA4_ACCESS_TOKEN:'fixture-token'},`
    assert.equal(opts.headers.Authorization,'Bearer fixture-token');
    return new Response(JSON.stringify({rows:[]}));`)
  assert.deepEqual(value(result),{rows:[]})
})
