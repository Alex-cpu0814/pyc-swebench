import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';

const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const n = spec.caseNumber;
if (!/^\d{3}$/.test(n)) throw new Error('Invalid case number');
const root = `E:/CLB_Swe-bench/pyc-swebench/Y_test_data/pyc_case_${n}`;
const read = rel => fs.readFileSync(path.join(root, rel), 'utf8');
const json = rel => JSON.parse(read(rel));
const check = (ok, msg) => { if (!ok) throw new Error(msg); };
const write = (rel, value) => fs.writeFileSync(path.join(root, rel), JSON.stringify(value, null, 2)+'\n');
const git = args => {
  const r = spawnSync('git', ['-C', spec.sourceRepo, ...args], {encoding:'utf8',maxBuffer:20*1024*1024});
  check(r.status === 0, r.stderr);
  return r.stdout;
};
check(spec.sourceRepo, 'sourceRepo required');
check(git(['rev-list','--parents','-n','1',spec.fixCommit]).trim().split(' ')[1] === spec.baseCommit, 'Parent mismatch');
const changed = git(['diff','--name-only',spec.baseCommit,spec.fixCommit]).trim().split('\n');
const testFiles = spec.testFiles ?? [spec.testFile];
const productFiles = changed.filter(p=>!testFiles.includes(p));
for (const [rel,files] of [['patches/gold_patch.diff',productFiles],['patches/test_patch.diff',testFiles]]) {
  check(read(rel) === git(['diff',...(spec.binaryPatches?['--binary']:[]),spec.baseCommit,spec.fixCommit,'--',...files]), `Not exact upstream: ${rel}`);
}
const gold = json(`verification/runs/case-${n}-final-gold/summary.json`);
const negative = json(`verification/runs/case-${n}-final-negative/summary.json`);
const tamper = json(`verification/runs/case-${n}-final-tamper/summary.json`);
const audit = json(`verification/builds/case-${n}-final-build/image-audit.json`);
let partialControl = null;
if (spec.partialControl) {
  check(read(spec.partialControl.patch) === git(['diff',spec.baseCommit,spec.fixCommit,'--',...spec.partialControl.productFiles]), 'Partial control is not exact upstream product-only diff');
  partialControl = json(spec.partialControl.summary);
  check(partialControl.status === 'unresolved' && partialControl.phase.phase === 'tests_complete', 'Partial control did not reach unresolved test execution');
  check(partialControl.grading.FAIL_TO_PASS.passed === 0 && partialControl.grading.PASS_TO_PASS.passed === spec.passToPass.length, 'Partial control target/regression mismatch');
  check(partialControl.phase.test_exit_code === spec.partialControl.expectedTestProcessExitCode, 'Partial control process exit mismatch');
}
check(gold.status === 'resolved' && gold.container_exit_code === 0, 'Gold not resolved');
check(gold.grading.FAIL_TO_PASS.passed === spec.failToPass.length && gold.grading.PASS_TO_PASS.passed === spec.passToPass.length, 'Gold grading mismatch');
check(negative.status === 'unresolved' && negative.phase.phase === 'tests_complete', 'Negative did not reach tests');
check(negative.grading.FAIL_TO_PASS.passed === 0 && negative.grading.PASS_TO_PASS.passed === spec.passToPass.length, 'Negative target/regression mismatch');
check(tamper.reason === 'candidate_conflicts_with_test_patch', 'Tamper not rejected');
check(audit.working_tree_clean && !audit.fix_commit_present && !audit.test_patch_present && !audit.gold_patch_present && !audit.model_patch_present, 'Image not clean');
const meta = json('official_swebench/metadata.json');
meta.verification.image = gold.image;
meta.verification.controls = {
  gold: {status:gold.status,reason:gold.reason,grading:gold.grading},
  negative: {status:negative.status,reason:negative.reason,grading:negative.grading},
  tamper: {status:tamper.status,reason:tamper.reason},
};
meta.verification.image_audit = audit;
if (partialControl) meta.verification.partial_python_only_control = {
  status: partialControl.status, reason: partialControl.reason,
  test_process_exit_code: partialControl.phase.test_exit_code,
  grading: partialControl.grading,
  observed_behavior: spec.partialControl.observedBehavior,
  summary: spec.partialControl.summary,
};
meta.verification.formal_runs = ['gold','negative','tamper'].map(label=>`verification/runs/case-${n}-final-${label}/summary.json`);
meta.product_files = productFiles;
meta.test_files = testFiles;
write('official_swebench/metadata.json', meta);
const files = [...new Set([
  `official_swebench/instance_${n}.json`, `official_swebench/instance_${n}.jsonl`,
  'official_swebench/metadata.json', `official_swebench/public_task_${n}.json`,
  'patches/gold_patch.diff','patches/test_patch.diff',
  `analysis/source_material/single_pyc_case_${n}.xlsx`, `analysis/source_row_${n}.json`,
  'analysis/environment_spec.json','analysis/upstream_provenance.json',
  'evaluator/case_config.json','evaluator/case_adapter.sh',
  ...(fs.existsSync(path.join(root,'evaluator/pytest_no_dump.py'))?['evaluator/pytest_no_dump.py']:[]),
  ...(spec.additionalRuntimeAssets ?? []).map(asset=>asset.source).filter(rel=>rel!=='evaluator/pytest_no_dump.py'),
  'evaluator/image/Dockerfile','evaluator/build_model_evaluator.py','evaluator/evaluate_model_patch.py',
  'evaluator/run_evaluation.sh','evaluator/logging_v3.py',
  'verification/controls/negative_patch.diff','verification/controls/tamper_patch.diff',
  `verification/builds/case-${n}-final-build/image-audit.json`,
  ...['gold','negative','tamper'].map(label=>`verification/runs/case-${n}-final-${label}/summary.json`),
  ...(spec.additionalVerificationAssets ?? []),
])];
fs.writeFileSync(path.join(root,'official_swebench/SHA256SUMS.txt'), files.map(rel=>`${crypto.createHash('sha256').update(fs.readFileSync(path.join(root,rel))).digest('hex')}  ${rel}\n`).join(''));
const repoRoot = 'E:/CLB_Swe-bench/pyc-swebench';
const readmePath = path.join(repoRoot,'README.md');
let readme = fs.readFileSync(readmePath,'utf8');
const row = `| \`pyc_case_${n}\` | \`${spec.repo}\` | Issue / PR #${spec.issueId} / commit \`${spec.fixCommit.slice(0,8)}\` | Base: ${spec.failToPass.length} target failures; Gold: ${spec.failToPass.length} targets and ${spec.passToPass.length} regressions pass |`;
if (!readme.includes(`| \`pyc_case_${n}\``)) {
  const last = [...readme.matchAll(/^\| `pyc_case_.*$/gm)].at(-1);
  check(last, 'Completed case table missing');
  readme = readme.slice(0,last.index+last[0].length)+'\n'+row+readme.slice(last.index+last[0].length);
  fs.writeFileSync(readmePath,readme);
}
console.log(`Finalized case ${n}; ${files.length} checksums; exact upstream diffs and formal controls verified.`);
