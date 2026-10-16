$ErrorActionPreference='Stop'
$caseRoot=[IO.Path]::GetFullPath('E:\CLB_Swe-bench\pyc-swebench\Y_test_data\pyc_case_091')
$source=[IO.Path]::GetFullPath((Join-Path $caseRoot 'verification\builds\case-091-final-build'))
$target=[IO.Path]::GetFullPath((Join-Path $caseRoot 'verification\history\formal-build-sandbox-temp-denial'))
if(-not $source.StartsWith($caseRoot+'\') -or -not $target.StartsWith($caseRoot+'\')){throw 'Unexpected scope'}
New-Item -ItemType Directory -Force -Path (Split-Path $target -Parent) | Out-Null
Move-Item -LiteralPath $source -Destination $target
@{status='infrastructure_failure';reason='Sandbox temporary-directory filesystem denial before Docker build';product_test_executed=$false;followup='Run authorized build with Docker/temp access in escalated context'} | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $target 'failure.json') -Encoding utf8
