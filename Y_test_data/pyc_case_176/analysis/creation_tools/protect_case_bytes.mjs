import fs from 'node:fs';
const n=process.argv[2],r='E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_'+n;
let lines=fs.readFileSync(r+'/.gitattributes','utf8').replace(/\r\n/g,'\n').trimEnd().split('\n');
function visit(d=''){for(const e of fs.readdirSync(r+(d?'/'+d:''),{withFileTypes:true})){const p=(d?d+'/':'')+e.name;if(e.isDirectory())visit(p);else if(!/\.(xlsx|png)$/.test(p)&&fs.readFileSync(r+'/'+p).includes(Buffer.from('\r\n')))lines.push('"'+p+'" -text');}}visit();
fs.writeFileSync(r+'/.gitattributes',[...new Set(lines)].join('\n')+'\n');
