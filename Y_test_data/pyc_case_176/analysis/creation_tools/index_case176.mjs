import fs from 'node:fs';
const p='E:/CLB_Swe-bench/pyc-swebench/README.md',lines=fs.readFileSync(p,'utf8').split('\n');let count=0;
for(let i=0;i<lines.length;i++)if(lines[i].startsWith('| `pyc_case_176` |')){lines[i]=lines[i].replace('Base: 1 target failures; Gold: 1 targets and 3 regressions pass','Base: JVM fatal SIGSEGV, process SIGABRT / terminal MISSING, 3 regressions pass; Gold: all 4 pass');count++;}
if(count!==1)throw Error('Exact one index row required');fs.writeFileSync(p,lines.join('\n'));
