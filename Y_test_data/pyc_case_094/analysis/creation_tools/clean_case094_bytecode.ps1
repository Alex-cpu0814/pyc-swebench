$ErrorActionPreference='Stop'
$caseRoot=[IO.Path]::GetFullPath('E:\CLB_Swe-bench\pyc-swebench\Y_test_data\pyc_case_094')
$target=[IO.Path]::GetFullPath((Join-Path $caseRoot 'evaluator\__pycache__'))
if($target -ne (Join-Path $caseRoot 'evaluator\__pycache__') -or -not $target.StartsWith($caseRoot+'\')){throw 'Unexpected cache target'}
if(Test-Path -LiteralPath $target){
 $entries=@(Get-ChildItem -LiteralPath $target -Recurse -Force)
 if(@($entries | Where-Object {($_.Attributes -band [IO.FileAttributes]::ReparsePoint) -or ((-not $_.PSIsContainer) -and $_.Extension -ne '.pyc')}).Count){throw 'Unexpected cache contents'}
 Remove-Item -LiteralPath $target -Recurse -Force
}
