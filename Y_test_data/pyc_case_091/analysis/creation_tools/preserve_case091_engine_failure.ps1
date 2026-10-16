$ErrorActionPreference='Stop'
$caseRoot=[IO.Path]::GetFullPath('E:\CLB_Swe-bench\pyc-swebench\Y_test_data\pyc_case_091')
$source=[IO.Path]::GetFullPath((Join-Path $caseRoot 'verification\builds\case-091-final-build'))
$target=[IO.Path]::GetFullPath((Join-Path $caseRoot 'verification\history\formal-build-missing-engine-pipe'))
if(-not $source.StartsWith($caseRoot+'\') -or -not $target.StartsWith($caseRoot+'\')){throw 'Unexpected scope'}
Move-Item -LiteralPath $source -Destination $target
$record=@{status='infrastructure_failure';reason='Docker Linux engine pipe missing before image build';product_test_executed=$false;docker_context='desktop-linux';endpoint='npipe:////./pipe/dockerDesktopLinuxEngine';error='The system cannot find the file specified';root_informed=$true}
[IO.File]::WriteAllText((Join-Path $target 'failure.json'),($record|ConvertTo-Json)+[char]10,(New-Object Text.UTF8Encoding($false)))
