import fs from 'node:fs';
const w='E:/CLB_Swe-bench/_work/pyc_batch',r='E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_177',old='E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_137',s=JSON.parse(fs.readFileSync(w+'/case177_spec.json','utf8'));
const prev=fs.readFileSync(old+'/evaluator/evaluate_model_patch.py','utf8'),p=r+'/evaluator/evaluate_model_patch.py',t=fs.readFileSync(p,'utf8'),a=t.indexOf('def parse_test_log(text):'),b=t.indexOf('\ndef expected_report(',a);if(a<0||b<0)throw Error('Parser missing');fs.writeFileSync(p,t.slice(0,a)+prev.slice(prev.indexOf('def parse_test_log(text):'),prev.indexOf('\ndef expected_report('))+t.slice(b));
fs.writeFileSync(r+'/evaluator/case_adapter.sh','#!/usr/bin/env bash\n\nbuild_project() {\n    '+s.buildCommand+'\n}\n\nrun_project_tests() {\n    '+s.testCommand+' \\\n'+s.probeNodes.map((n,i)=>"        '"+n+"'"+(i<s.probeNodes.length-1?' \\':'')).join('\n')+'\n}\n');
console.log('177 canonical parser and identical P2P→F2P original-method order configured.');
const builder=r+'/evaluator/build_model_evaluator.py';fs.writeFileSync(builder,fs.readFileSync(builder,'utf8').replace('python --version','python2.7 --version'));
