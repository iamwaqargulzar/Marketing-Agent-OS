const { test } = require('node:test')
const assert = require('node:assert/strict')
const { spawnSync } = require('node:child_process')
const path = require('node:path')
const cli = path.resolve(__dirname, '../../tools/clis/github-prospects.js')
function exportUsers(users, format) {
  const source = `global.fetch = async () => ({ ok: true, status: 200, headers: new Headers(), json: async () => ${JSON.stringify(users)} }); process.argv = ['node', ${JSON.stringify(cli)}, 'stargazers', 'example/repo', '--format', ${JSON.stringify(format)}]; require(${JSON.stringify(cli)});`
  const result = spawnSync(process.execPath, ['-e', source], { encoding: 'utf8' })
  assert.equal(result.status, 0, result.stderr)
  return result.stdout.trimEnd()
}
// Parse CSV independently to check the actual exported cells, not source text.
function cells(row) {
  const result = []; let field = ''; let quoted = false
  for (let i = 0; i < row.length; i++) {
    const ch = row[i]
    if (ch === '"') {
      if (quoted && row[i+1] === '"') { field += '"'; i++ }
      else quoted = !quoted
    } else if (ch === ',' && !quoted) { result.push(field); field = '' }
    else field += ch
  }
  result.push(field); return result
}
for (const value of ['=1+1', '+1+1', '-1+1', '@SUM(1,2)', '\t=1+1', '\r=1+1', '\n=1+1']) {
  test(`CSV exports formula-like profile text as literal: ${JSON.stringify(value)}`, () => {
    const rows = exportUsers([{login: 'user', name: value}], 'csv').split('\n')
    assert.ok(cells(rows[1])[1].startsWith("'"))
  })
}
test('ordinary commas and quotes remain valid CSV and numeric fields stay numeric', () => {
  const row = cells(exportUsers([{ login: 'user', name: 'Doe, "Jane"', company: 'Ordinary', followers: 12 }], 'csv').split('\n')[1])
  assert.equal(row[1], 'Doe, "Jane"'); assert.equal(row[2], 'Ordinary'); assert.equal(row[9], '12')
})
test('JSON preserves the original profile data', () => {
  const user = { login: 'user', name: '=1+1' }
  assert.deepEqual(JSON.parse(exportUsers([user], 'json')).users, [user])
})
