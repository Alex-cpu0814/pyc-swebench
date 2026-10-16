param([Parameter(Mandatory=$true)][string]$PublishedCommit)
$ErrorActionPreference='Stop'
if($PublishedCommit -notmatch '^[0-9a-f]{40}$'){throw 'Invalid commit'}
$taskRoot=[IO.Path]::GetFullPath('E:\CLB_Swe-bench\_work\pyc_batch')
$repository='E:\CLB_Swe-bench\pyc-swebench'
$archive=[IO.Path]::GetFullPath((Join-Path $repository 'Y_test_data\pyc_case_159\analysis\prior_candidate_reviews\case157'))
$actual=git -C $repository rev-parse HEAD
if($LASTEXITCODE -ne 0 -or $actual.Trim() -ne $PublishedCommit){throw 'Wrong committed archive'}
$helpers=@('Dockerfile.pysqlite157-local','preflight_case157_platform.mjs','initialize_case157.py','prepare_case157_audit.py','audit_case157.mjs','configure_case157_formal.mjs','correct_case157_platform.py','build_case157_prototype.mjs','fetch_case157_sources.py','review_case157_sqlite_history.py','defer_case157.py')
$targets=@(Get-ChildItem -LiteralPath $taskRoot | Where-Object {($_.Name.StartsWith('case157') -or $_.Name -in $helpers) -and $_.Name -notin @('case157_progress.md','case157_cleanup.json')})
$fileCount=0;$directoryCount=0;$byteCount=0
foreach($item in $targets){
 $resolved=[IO.Path]::GetFullPath($item.FullName)
 if(-not $resolved.StartsWith($taskRoot+'\') -or ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)){throw 'Unsafe target'}
 $copyRoot=if($item.Name -eq 'case157-deferred-review'){$archive}else{Join-Path $archive $item.Name}
 $files=if($item.PSIsContainer){@(Get-ChildItem -LiteralPath $resolved -Recurse -File)}else{@($item)}
 foreach($file in $files){
  if($file.Attributes -band [IO.FileAttributes]::ReparsePoint){throw 'Reparse file'}
  $copy=if($item.PSIsContainer){Join-Path $copyRoot $file.FullName.Substring($resolved.Length+1)}else{$copyRoot}
  if(-not (Test-Path -LiteralPath $copy -PathType Leaf) -or (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash -ne (Get-FileHash -LiteralPath $copy -Algorithm SHA256).Hash){throw ('Unarchived bytes: '+$file.FullName)}
  $fileCount++;$byteCount+=$file.Length
 }
 if($item.PSIsContainer){$children=@(Get-ChildItem -LiteralPath $resolved -Recurse -Directory);if(@($children|Where-Object {$_.Attributes -band [IO.FileAttributes]::ReparsePoint}).Count){throw 'Reparse directory'};$directoryCount+=1+$children.Count}
}
foreach($item in $targets){Remove-Item -LiteralPath $item.FullName -Recurse -Force}
$report=@{caseNumber='157';status='deferred_evidence_archived_cleaned';archiveCommit=$PublishedCommit;archive=$archive;filesRemoved=$fileCount;directoriesRemoved=$directoryCount;bytesRemoved=$byteCount;targets=@($targets.Name)}
[IO.File]::WriteAllText((Join-Path $taskRoot 'case157_cleanup.json'),($report|ConvertTo-Json -Depth 5)+[char]10,(New-Object Text.UTF8Encoding($false)))
$report|ConvertTo-Json -Depth 5
