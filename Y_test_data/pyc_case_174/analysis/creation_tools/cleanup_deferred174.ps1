param([Parameter(Mandatory=$true)][string]$PublishedCommit)
$ErrorActionPreference='Stop'
$taskWork=[IO.Path]::GetFullPath('E:\CLB_Swe-bench\_work\pyc_batch')
$taskCase=[IO.Path]::GetFullPath('E:\CLB_Swe-bench\pyc-swebench\Y_test_data\pyc_case_174')
$taskHead=git -C 'E:\CLB_Swe-bench\pyc-swebench' rev-parse HEAD
if($LASTEXITCODE -ne 0 -or $taskHead.Trim() -ne $PublishedCommit){throw 'Commit differs'}
$taskTargets=Get-Content -LiteralPath (Join-Path $taskCase 'analysis\creation_tools\deferred_cleanup_targets174.json') -Raw | ConvertFrom-Json
$taskCount=0
foreach($taskTarget in $taskTargets){
 $taskSource=[IO.Path]::GetFullPath($taskTarget.source)
 $taskArchive=[IO.Path]::GetFullPath($taskTarget.archive)
 if(-not $taskSource.StartsWith($taskWork+'\') -or -not $taskArchive.StartsWith($taskCase+'\analysis\prior_candidate_reviews\')){throw 'Unsafe resolved path'}
 $taskItem=Get-Item -LiteralPath $taskSource
 if($taskItem.Attributes -band [IO.FileAttributes]::ReparsePoint){throw 'Reparse point'}
 $taskFiles=if($taskItem.PSIsContainer){@(Get-ChildItem -LiteralPath $taskSource -Recurse -File)}else{@($taskItem)}
 foreach($taskFile in $taskFiles){
  $taskSaved=if($taskItem.PSIsContainer){Join-Path $taskArchive $taskFile.FullName.Substring($taskSource.Length+1)}else{$taskArchive}
  if(-not(Test-Path -LiteralPath $taskSaved -PathType Leaf) -or (Get-FileHash -LiteralPath $taskFile.FullName -Algorithm SHA256).Hash -ne (Get-FileHash -LiteralPath $taskSaved -Algorithm SHA256).Hash){throw ('Unarchived bytes '+$taskFile.FullName)}
  $taskCount++
 }
}
foreach($taskTarget in $taskTargets){Remove-Item -LiteralPath $taskTarget.source -Recurse -Force}
$taskReport=@{status='archived_deferred_scratch_cleaned';publishedCommit=$PublishedCommit;targets=$taskTargets.Count;filesRemoved=$taskCount;preserved=@('frozen evidence in case174','shared source caches','prior case progress notes')}
[IO.File]::WriteAllText((Join-Path $taskWork 'case174_deferred_cleanup.json'),($taskReport|ConvertTo-Json -Depth 4)+[char]10,[Text.UTF8Encoding]::new($false))
$taskReport|ConvertTo-Json -Depth 4
