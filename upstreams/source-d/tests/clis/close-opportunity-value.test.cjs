const {test}=require('node:test')
const assert=require('node:assert/strict')
const {spawnSync}=require('node:child_process')
const path=require('node:path')
const cli=path.resolve(__dirname,'../../tools/clis/close.js')
function run(value,preview=false){
 const args=['opportunities','create','--lead-id','lead_fixture','--value'];if(value!==undefined)args.push(value);if(preview)args.push('--dry-run')
 const source=`global.fetch=async(url,opts)=>{process.stderr.write('FETCH_CALLED');return {status:200,text:async()=>JSON.stringify({body:JSON.parse(opts.body),headers:opts.headers})}};process.argv=['node',${JSON.stringify(cli)},...${JSON.stringify(args)}];require(${JSON.stringify(cli)})`
 return spawnSync(process.execPath,['-e',source],{encoding:'utf8',env:{...process.env,CLOSE_API_KEY:'fixture-key'},timeout:5000})
}
test('rejects lossy or nonnumeric opportunity values before delivery or preview',()=>{
 for(const value of [undefined,'',' ','12.9','12abc','NaN','Infinity','1e309','9007199254740992'])for(const preview of [false,true]){
  const r=run(value,preview);assert.equal(r.status,1,`${value}: ${r.stdout}`);assert.equal(r.stderr.includes('FETCH_CALLED'),false);assert.match(JSON.parse(r.stderr).error,/safe integer/)
 }
})
test('retains exact integer amounts including zero and scientific notation',()=>{
 for(const value of ['0','1250','-25','1e3','10.0','9007199254740991'])for(const preview of [false,true]){
  const r=run(value,preview);assert.equal(r.status,0,r.stderr);const output=JSON.parse(r.stdout);assert.equal(output.body.value,Number(value));assert.equal(output.body.lead_id,'lead_fixture');assert.equal(output.headers.Authorization,preview?'Basic ***':`Basic ${Buffer.from('fixture-key:').toString('base64')}`)
 }
})
