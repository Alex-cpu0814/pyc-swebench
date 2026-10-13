import fs from 'node:fs';import crypto from 'node:crypto';
const work='E:/CLB_Swe-bench/_work/pyc_batch',root='E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_060',p=root+'/evaluator/evaluate_model_patch.py',old=fs.readFileSync(p,'utf8'),dir=root+'/verification/parser-history';fs.mkdirSync(dir);fs.writeFileSync(dir+'/evaluate_model_patch_initial.py',old);fs.writeFileSync(dir+'/summary.json',JSON.stringify({initial_sha256:crypto.createHash('sha256').update(old).digest('hex'),reason:'Template pytest regex did not recognize annotated native process failure; initial negative grading showed targets MISSING despite explicit SIGSEGV records. Final parser recognizes validated ISOLATED_NODE_RESULT native signal JSON as node failure.',scope:'Only Case060 evaluator parser; official tests/runtime/product patches unchanged.'},null,2)+'\n');
const anchor='        pytest_match = PYTEST_LINE.match(line)',insert=`        if "ISOLATED_NODE_RESULT " in line:
            process = json.loads(line.split("ISOLATED_NODE_RESULT ", 1)[1])
            if (process.get("returncode") == -11
                    and process.get("signal") == "SIGSEGV"
                    and process.get("node", "").startswith("Tests/")):
                statuses[process["node"]] = "FAILED"
                pending = None
                continue
`;
if(!old.includes(anchor))throw new Error('Parser anchor missing');fs.writeFileSync(p,old.replace(anchor,insert+anchor));fs.renameSync(root+'/verification/runs/case-060-final-negative',root+'/verification/runs/case-060-final-negative-initial-parser');const sp=work+'/case060_spec.json',s=JSON.parse(fs.readFileSync(sp,'utf8'));s.additionalVerificationAssets.push('verification/parser-history/evaluate_model_patch_initial.py','verification/parser-history/summary.json','verification/runs/case-060-final-negative-initial-parser/summary.json','verification/runs/case-060-final-negative-initial-parser/tests.raw.log','verification/runs/case-060-final-negative-initial-parser/grading.json');s.provenance.parser_history='verification/parser-history/summary.json';fs.writeFileSync(sp,JSON.stringify(s,null,2)+'\n');console.log('Case060 process-signal parser corrected; initial parser and negative logs preserved.');
