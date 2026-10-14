const {test}=require('node:test')
const assert=require('node:assert/strict')
const {spawnSync}=require('node:child_process')
const path=require('node:path')
const cli=path.resolve(__dirname,'../../tools/clis/pendo.js')
function run(resource,value,preview=false){
 const args=[resource,'search','--query',value];if(preview)args.push('--dry-run')
 const source=`global.fetch=async(url,opts)=>{process.stderr.write('FETCH_CALLED');return {status:200,text:async()=>JSON.stringify({url,body:JSON.parse(opts.body),headers:opts.headers})}};process.argv=['node',${JSON.stringify(cli)},...${JSON.stringify(args)}];require(${JSON.stringify(cli)})`
 return spawnSync(process.execPath,['-e',source],{encoding:'utf8',env:{...process.env,PENDO_INTEGRATION_KEY:'fixture-key'},timeout:5000})
}
test('rejects non-aggregation search queries before delivery or preview',()=>{
 for(const resource of ['visitors','accounts'])for(const value of ['null','[]','true','42','"text"','{}','{"request":null}','{"request":[]}','{"request":{"pipeline":{}}}'])for(const preview of [false,true]){
  const result=run(resource,value,preview);assert.equal(result.status,1);assert.equal(result.stderr.includes('FETCH_CALLED'),false);assert.match(JSON.parse(result.stderr).error,/aggregation object with request.pipeline as an array/)
 }
})
test('preserves complete search envelopes and masking',()=>{
 for(const resource of ['visitors','accounts'])for(const preview of [false,true]){
  const body={response:{mimeType:'application/json'},request:{requestId:'fixture',pipeline:[{source:{[resource]:null}},{limit:10}]}}
  const result=run(resource,JSON.stringify(body),preview);assert.equal(result.status,0,result.stderr);const output=JSON.parse(result.stdout);assert.deepEqual(output.body,body);assert.equal(output.headers['x-pendo-integration-key'],preview?'***':'fixture-key');assert.match(output.url,/\/aggregation$/)
 }
})
test('preserves malformed search-query diagnostics',()=>{
 for(const resource of ['visitors','accounts']){const result=run(resource,'{broken');assert.equal(result.stderr.includes('FETCH_CALLED'),false);assert.equal(JSON.parse(result.stdout).error,'Invalid JSON in --query')}
})
