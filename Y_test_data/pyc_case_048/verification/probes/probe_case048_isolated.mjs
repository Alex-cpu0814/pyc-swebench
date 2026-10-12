import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
const label = process.argv[2];
if (!['base', 'gold'].includes(label)) throw new Error('Use base or gold');
const work = 'E:/CLB_Swe-bench/_work/pyc_batch';
const spec = JSON.parse(fs.readFileSync(path.join(work, 'case048_spec.json'), 'utf8'));
const out = path.join(work, `case048-probe-${label}-isolated`);
fs.mkdirSync(out);
const docker = 'C:/Users/玉兔/AppData/Local/Programs/DockerDesktop/resources/bin/docker.exe';
const args = ['run', '--rm', '--network', 'none', ...spec.dockerRunArgs];
for (const [source,target] of [[spec.goldPatchSource,'/tmp/gold.diff'], [spec.testPatchSource,'/tmp/test.diff'],
  [path.join(work,'pytest_no_dump.py'),'/benchmark/pytest_no_dump.py'],
  [path.join(work,'pytest_case048_isolated.py'),'/benchmark/pytest_case048_isolated.py']]) {
  args.push('--mount', `type=bind,source=${source},target=${target},readonly`);
}
const nodes = [...spec.passToPass, ...spec.failToPass];
const cmd = ['set -euo pipefail', 'git apply --check /tmp/gold.diff', 'git apply --check /tmp/test.diff',
  ...(label === 'gold' ? ['git apply /tmp/gold.diff'] : []), 'git apply /tmp/test.diff',
  'touch scipy/signal/sigtoolsmodule.c',
  'CFLAGS="-O0 -g -fsanitize=bounds -fno-sanitize-recover=bounds" LDFLAGS="-fsanitize=bounds" python setup.py build_ext -i >/tmp/build-bounds.log 2>&1 || { tail -80 /tmp/build-bounds.log; exit 2; }',
  'UBSAN_OPTIONS=halt_on_error=1:print_stacktrace=1 python /benchmark/pytest_case048_isolated.py ' + nodes.map(n=>`'${n}'`).join(' '),
].join('; ');
args.push('--entrypoint','/bin/bash','pyc-case048-prototype-base:latest','-lc',cmd);
const startedAt = new Date().toISOString();
const r = spawnSync(docker,args,{encoding:'utf8',timeout:600000,maxBuffer:64*1024*1024,windowsHide:true});
fs.writeFileSync(path.join(out,'stdout.raw.log'), r.stdout ?? '');
fs.writeFileSync(path.join(out,'stderr.raw.log'), r.stderr ?? '');
const summary = {label,image:'pyc-case048-prototype-base:latest',instrumentation:'GCC 10 non-recovering bounds sanitizer; identical flags on Base and Gold; official nodes isolated in subprocesses',nodes,startedAt,finishedAt:new Date().toISOString(),exitCode:r.status,error:r.error?.message ?? null,command:[docker,...args]};
fs.writeFileSync(path.join(out,'summary.json'),JSON.stringify(summary,null,2)+'\n');
console.log(JSON.stringify({label,exitCode:r.status,error:summary.error}));
console.log((r.stdout ?? '').slice(-7000));
console.log((r.stderr ?? '').slice(-2000));
