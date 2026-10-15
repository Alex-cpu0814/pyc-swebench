import fs from 'node:fs';
const r='E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_088',p=r+'/evaluator/evaluate_model_patch.py';
let t=fs.readFileSync(p,'utf8');
const start=t.indexOf('def parse_test_log(text):'),end=t.indexOf('\ndef expected_report(',start);
if(start<0||end<0)throw Error('Parser function missing');
t=t.slice(0,start)+`def parse_test_log(text):
    # Official wrapper owns terminal statuses after checking true child results.
    # Human-readable bundled-unittest output is retained but is not a second ID.
    statuses = {}
    for line in text.splitlines():
        match = PYTEST_LINE.fullmatch(line)
        if match:
            statuses[match.group("test_id")] = match.group("status")
    return statuses

`+t.slice(end);
fs.writeFileSync(p,t);
const history=r+'/verification/history/formal-parser-v1';fs.mkdirSync(history,{recursive:true});
for(const label of ['gold','negative']){
 const src=r+'/verification/runs/case-088-final-'+label,dst=history+'/case-088-final-'+label;
 if(fs.existsSync(src)&&!fs.existsSync(dst))fs.renameSync(src,dst);
}
console.log('Preserved initial double-counting parser evidence; terminal official node statuses only.');
