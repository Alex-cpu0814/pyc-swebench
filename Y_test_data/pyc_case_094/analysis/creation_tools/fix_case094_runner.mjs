import fs from 'node:fs';
const w='E:/CLB_Swe-bench/_work/pyc_batch',p=w+'/legacy_unittest094.py',before=fs.readFileSync(p,'utf8');
fs.writeFileSync(w+'/legacy_unittest094_initial.py',before);
const marker="    if len(records) == 1 and records[0]['node'] == node and records[0]['testsRun'] == 1:";
if(!before.includes(marker))throw Error('Runner pattern missing');
const after=before.replace(marker,`    # An actual native crash after official method start is always a failure,
    # including a crash during shutdown after TextTestRunner emitted its result.
    # The original result and every stdout/stderr byte remain in the record.
    if child.returncode in (-signal.SIGSEGV, -signal.SIGABRT) and 'OFFICIAL_TEST_START ' + node in lines:
        status = 'FAILED'
        print('OFFICIAL_NATIVE_FAILURE ' + json.dumps({'node': node, 'returncode': child.returncode,
            'signal': signal.Signals(-child.returncode).name,
            'reported_results': records}), flush=True)
    elif len(records) == 1 and records[0]['node'] == node and records[0]['testsRun'] == 1:`);
fs.writeFileSync(p,after);
const q=w+'/case094_spec.json',s=JSON.parse(fs.readFileSync(q,'utf8'));s.probeSuffixes={base:'-v2',gold:'',collect:''};
s.testExecution='Full original official methods use bundled TestLoader/TextTestRunner once per fresh child. PASSED requires testsRun1/wasSuccessful plus normal exit. SIGSEGV/SIGABRT after actual OFFICIAL_TEST_START is FAILED even if the original runner emitted a result before shutdown; original stdout/stderr, result, native signal and true process exit remain losslessly recorded. Missing loader/results without such a genuine started-method signal are infrastructure errors. No test body/input/assertion/compiler/allocator changes.';
fs.writeFileSync(q,JSON.stringify(s,null,2)+'\n');
fs.writeFileSync(w+'/case094_runner_correction.json',JSON.stringify({reason:'Initial Base has genuine official testsRun1/failures1 report followed by childSIGSEGV; original wrapper mislabeled the recorded failure plus abnormal shutdown as infrastructure ERROR.',fix:'Classify native SIGSEGV/SIGABRT after OFFICIAL_TEST_START as FAILED before ordinary result/exit consistency checks; preserve full raw/encoded result and exact exit. Never turn abnormal exit into PASSED.',initial_evidence:'case094-probe-base',base_repeat_suffix:'-v2',successful_gold_repeated:false,product_or_test_source_modified:false},null,2)+'\n');
console.log('094 genuine started-method crash classification corrected without altering tests.');
