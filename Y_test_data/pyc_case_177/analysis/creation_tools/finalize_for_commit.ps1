param([Parameter(Mandatory=$true)][ValidatePattern('^[0-9]{3}$')][string]$Number)
$ErrorActionPreference='Stop'
$taskWork='E:/CLB_Swe-bench/_work/pyc_batch'
$taskPython='C:/Users/玉兔/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
$taskNode='C:/Users/玉兔/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
& $taskNode ($taskWork+'/document_native_case.mjs') $Number
if($LASTEXITCODE -ne 0){throw 'Document archive failed'}
& $taskNode ($taskWork+'/protect_case_bytes.mjs') $Number
if($LASTEXITCODE -ne 0){throw 'Byte protection failed'}
& $taskNode ($taskWork+'/refresh_case'+$Number+'.mjs')
if($LASTEXITCODE -ne 0){throw 'Asset coverage failed'}
& $taskNode ($taskWork+'/finalize_case.mjs') ($taskWork+'/case'+$Number+'_spec.json')
if($LASTEXITCODE -ne 0){throw 'Finalize failed'}
& $taskNode ($taskWork+'/validate_case.mjs') $Number
if($LASTEXITCODE -ne 0){throw 'Consistency failed'}
& $taskPython -B ($taskWork+'/independent_case_review.py') $Number --hashes
if($LASTEXITCODE -ne 0){throw 'Evidence review failed'}
& $taskNode ($taskWork+'/commit_case'+$Number+'.mjs')
if($LASTEXITCODE -ne 0){throw 'Scoped commit failed'}
& $taskPython -B ($taskWork+'/independent_case_review.py') $Number --hashes --committed
if($LASTEXITCODE -ne 0){throw 'Committed blob review failed'}
git -C 'E:/CLB_Swe-bench/pyc-swebench' diff HEAD^ HEAD -- README.md
