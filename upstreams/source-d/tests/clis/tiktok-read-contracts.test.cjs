const assert = require('node:assert/strict')
const { spawnSync } = require('node:child_process')
const fs = require('node:fs')
const os = require('node:os')
const path = require('node:path')
const { test } = require('node:test')

const cli = path.resolve(__dirname, '../../tools/clis/tiktok-ads.js')
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

const env = { TIKTOK_ACCESS_TOKEN: 'fixture-token', TIKTOK_ADVERTISER_ID: '12345' }
const reportArgs = ['reports', 'get', '--start-date', '2026-09-01', '--end-date', '2026-09-30']
const reportOracle = `
  const query = new URL(url).searchParams;
  assert.equal(new URL(url).pathname, '/open_api/v1.3/report/integrated/get/');
  assert.equal(opts.method, 'GET'); assert.equal(opts.body, undefined);
  assert.equal(query.get('advertiser_id'), '12345'); assert.equal(query.get('report_type'), 'BASIC');
  assert.equal(query.get('start_date'), '2026-09-01'); assert.equal(query.get('end_date'), '2026-09-30');
  assert.deepEqual(JSON.parse(query.get('dimensions')), ['campaign_id']);
  assert.deepEqual(JSON.parse(query.get('metrics')), ['spend', 'impressions', 'clicks', 'conversion']);
  return new Response(JSON.stringify({code:0,data:{list:[{spend:'42.00'}]}}));`
test('synchronous reports use the documented GET query contract', () => {
  assert.equal(value(run(reportArgs, env, reportOracle)).data.list[0].spend, '42.00')
})
test('campaign filter is nested in adgroup filtering', () => {
  const result = run(['adgroups', 'list', '--campaign-id', 'campaign42'], env, `
    const query = new URL(url).searchParams;
    assert.equal(opts.method, 'GET'); assert.equal(query.has('campaign_ids'), false);
    assert.deepEqual(JSON.parse(query.get('filtering')), {campaign_ids:['campaign42']});
    return new Response(JSON.stringify({code:0,data:{list:[{campaign_id:'campaign42'}]}}));`)
  assert.equal(value(result).data.list[0].campaign_id, 'campaign42')
})
test('report dry-run uses the same GET contract and masks credentials', () => {
  const result = run([...reportArgs, '--dry-run'], env)
  const preview = value(result)
  assert.equal(preview.method, 'GET'); assert.equal(preview.body, undefined)
  assert.deepEqual(JSON.parse(new URL(preview.url).searchParams.get('dimensions')), ['campaign_id'])
  assert.equal(result.stdout.includes('fixture-token'), false)
})
test('campaign creation remains POST JSON', () => {
  const result = run(['campaigns', 'create', '--name', 'Fixture', '--objective', 'TRAFFIC'], env, `
    assert.equal(opts.method,'POST'); const body=JSON.parse(opts.body);
    assert.equal(body.campaign_name,'Fixture'); assert.equal(body.advertiser_id,'12345');
    return new Response(JSON.stringify({code:0,data:{campaign_id:'new42'}}));`)
  assert.equal(value(result).data.campaign_id, 'new42')
})
