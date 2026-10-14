const {test}=require('node:test')
const assert=require('node:assert/strict')
const {spawnSync}=require('node:child_process')
const path=require('node:path')
const cli=path.resolve(__dirname,'../../tools/clis/resend.js')
function run(value,preview=false,sub="create"){
 const args=['templates',sub,'fixture-id','--name','Fixture','--html','<p>Hi</p>'];if(value!==undefined)args.push('--variables',value);if(preview)args.push('--dry-run')
 const source=`global.fetch=async(url,opts)=>{process.stderr.write('FETCH_CALLED');return {status:200,text:async()=>JSON.stringify({body:JSON.parse(opts.body),headers:opts.headers})}};process.argv=['node',${JSON.stringify(cli)},...${JSON.stringify(args)}];require(${JSON.stringify(cli)})`
 return spawnSync(process.execPath,['-e',source],{encoding:'utf8',env:{...process.env,RESEND_API_KEY:'fixture-key'},timeout:5000})
}
const variable={key:'NAME',type:'string',fallback_value:'Reader'}
test('rejects invalid variable containers, entries, and sizes before delivery or preview',()=>{
 for(const value of ['null','{}','true','42','"text"','[null]','[[]]','[42]',JSON.stringify(Array(51).fill(variable))])for(const preview of [false,true])for(const sub of ["create","update"]){
  const result=run(value,preview,sub);assert.equal(result.status,1,`${value}: ${result.stdout}`);assert.equal(result.stderr.includes('FETCH_CALLED'),false);assert.match(JSON.parse(result.stderr).error,/array of up to 50 variable objects/);assert.equal(result.stdout,'')
 }
})
test('zero, one and fifty variables retain payload and masking',()=>{
 for(const count of [0,1,50])for(const preview of [false,true])for(const sub of ["create","update"]){const variables=Array.from({length:count},(_,i)=>({key:`FIXTURE_${i}`,type:i%2 ? "number" : "string",fallback_value:i%2 ? 25 : "Reader"}));const result=run(JSON.stringify(variables),preview,sub);assert.equal(result.status,0,result.stderr);const response=JSON.parse(result.stdout);assert.deepEqual(response.body.variables,variables);assert.equal(response.headers.Authorization,preview?'***':'Bearer fixture-key')}
})
test('retains malformed JSON diagnostic without delivery',()=>{
 const result=run('{broken');assert.equal(result.stderr.includes('FETCH_CALLED'),false);assert.match(JSON.parse(result.stdout).error,/Invalid JSON for --variables:/)
})
test('omitted optional variables remain absent for creation and update',()=>{
 for(const sub of ['create','update'])for(const preview of [false,true]){
  const result=run(undefined,preview,sub);assert.equal(result.status,0,result.stderr);assert.equal(Object.hasOwn(JSON.parse(result.stdout).body,'variables'),false)
 }
})
