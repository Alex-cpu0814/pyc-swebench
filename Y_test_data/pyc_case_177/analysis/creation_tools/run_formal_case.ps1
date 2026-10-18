param([Parameter(Mandatory=$true)][ValidatePattern('^[0-9]{3}$')][string]$Number)
$ErrorActionPreference='Stop'
$taskRoot='E:/CLB_Swe-bench'
$taskCase=Join-Path $taskRoot ('pyc-swebench/Y_test_data/pyc_case_'+$Number)
$taskPython='C:/Users/玉兔/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
$taskNode='C:/Users/玉兔/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
$taskDocker='C:/Users/玉兔/AppData/Local/Programs/DockerDesktop/resources/bin/docker.exe'
& $taskPython -B ($taskCase+'/evaluator/build_model_evaluator.py') --docker $taskDocker --build-id ('case-'+$Number+'-final-build')
if($LASTEXITCODE -ne 0){throw 'Formal build failed'}
& $taskNode ($taskRoot+'/_work/pyc_batch/audit_case'+$Number+'.mjs') --formal
if($LASTEXITCODE -ne 0){throw 'Formal audit failed'}
foreach($taskLabel in @('gold','negative','tamper')){
 $taskPatch=if($taskLabel -eq 'gold'){$taskCase+'/patches/gold_patch.diff'}else{$taskCase+'/verification/controls/'+$taskLabel+'_patch.diff'}
 & $taskPython -B ($taskCase+'/evaluator/evaluate_model_patch.py') --patch $taskPatch --docker $taskDocker --run-id ('case-'+$Number+'-final-'+$taskLabel) --label $taskLabel
 if($taskLabel -eq 'gold' -and $LASTEXITCODE -ne 0){throw 'Gold did not resolve'}
}
foreach($taskLabel in @('gold','negative','tamper')){
 $taskSummary=Get-Content -LiteralPath ($taskCase+'/verification/runs/case-'+$Number+'-final-'+$taskLabel+'/summary.json') -Raw|ConvertFrom-Json
 [pscustomobject]@{Label=$taskLabel;Status=$taskSummary.status;Reason=$taskSummary.reason;Exit=$taskSummary.phase.test_exit_code}
}
