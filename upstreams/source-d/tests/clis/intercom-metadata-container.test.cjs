const {test}=require('node:test')
const assert=require('node:assert/strict')
const {spawnSync}=require('node:child_process')
const path=require('node:path')
const cli=path.resolve(__dirname,'../../tools/clis/intercom.js')
function run(value,preview=false){const args=['events','create','--name','Purchased','--user-id','fixture','--metadata',value];if(preview)args.push('--dry-run');const source=`global.fetch=async(url,opts)=>{process.stderr.write('FETCH_CALLED');return {status:200,text:async()=>JSON.stringify({body:JSON.parse(opts.body)})}};process.argv=['node',${JSON.stringify(cli)},...${JSON.stringify(args)}];require(${JSON.stringify(cli)})`;return spawnSync(process.execPath,['-e',source],{encoding:'utf8',env:{...process.env,INTERCOM_API_KEY:'fixture-key'},timeout:5000})}
test('rejects metadata containers incompatible with the event object contract',()=>{for(const value of ['null','[]','true','42','"text"'])for(const preview of [false,true]){const r=run(value,preview);assert.equal(r.status,1,r.stdout);assert.equal(r.stderr.includes('FETCH_CALLED'),false);assert.match(JSON.parse(r.stderr).error,/must be a JSON object/);assert.equal(r.stdout,'')}})
test('preserves empty and nested metadata dictionaries in delivery and preview',()=>{for(const metadata of [{},{item:'Pro',price:{amount:9900,currency:'usd'}}])for(const preview of [false,true]){const r=run(JSON.stringify(metadata),preview);assert.equal(r.status,0,r.stderr);assert.deepEqual(JSON.parse(r.stdout).body.metadata,metadata)}})
