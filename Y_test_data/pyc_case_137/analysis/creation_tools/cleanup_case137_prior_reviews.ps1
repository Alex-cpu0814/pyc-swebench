param([string]$PublishedCommit,[switch]$PreviewOnly)
$ErrorActionPreference='Stop'
$workRoot=[IO.Path]::GetFullPath('E:\CLB_Swe-bench\_work\pyc_batch')
$repoRoot='E:\CLB_Swe-bench\pyc-swebench'
$caseRoot=[IO.Path]::GetFullPath((Join-Path $repoRoot 'Y_test_data\pyc_case_137'))
if(-not $PreviewOnly){
 if($PublishedCommit -notmatch '^[0-9a-f]{40}$'){throw 'Invalid commit'}
 $head=git -C $repoRoot rev-parse HEAD
 if($LASTEXITCODE -ne 0 -or $head.Trim() -ne $PublishedCommit){throw 'Published commit mismatch'}
 $publication=Get-Content -LiteralPath (Join-Path $caseRoot 'verification\publication\publication.json') -Raw | ConvertFrom-Json
 if($publication.image -ne 'yutu0814/pyc-case-137-pycairo:benchmark-v1'){throw 'Wrong formal publication'}
}
$numbers=@('106','107','111','113','114','128','132','134')
$items=@();$fileCount=0;$directoryCount=0;$byteCount=0
foreach($number in $numbers){
 $archiveRoot=[IO.Path]::GetFullPath((Join-Path $caseRoot ('analysis\prior_candidate_reviews\case'+$number)))
 if(-not $archiveRoot.StartsWith($caseRoot+'\')){throw 'Unexpected archive scope'}
 $reviewName=if([int]$number -lt 128){'case'+$number+'-platform-review'}else{'case'+$number+'-deferred-review'}
 $targets=@(Get-ChildItem -LiteralPath $workRoot -Force | Where-Object {$_.Name.Contains($number) -and $_.Name -notin @(('case'+$number+'_progress.md'),('case'+$number+'_cleanup.json'))})
 foreach($target in $targets){
  $resolved=[IO.Path]::GetFullPath($target.FullName)
  if(-not $resolved.StartsWith($workRoot+'\') -or ($target.Attributes -band [IO.FileAttributes]::ReparsePoint)){throw 'Unsafe source target'}
  $destination=if($target.Name -eq $reviewName){$archiveRoot}elseif($target.PSIsContainer){Join-Path $archiveRoot ('evidence\'+$target.Name)}elseif([int]$number -ge 128){Join-Path $archiveRoot ('creation_tools\'+$target.Name)}elseif($target.Name -eq ('case'+$number+'_review_spec.json')){Join-Path $archiveRoot 'review_spec.json'}else{Join-Path $archiveRoot $target.Name}
  $destination=[IO.Path]::GetFullPath($destination)
  if($destination -ne $archiveRoot -and -not $destination.StartsWith($archiveRoot+'\')){throw 'Unsafe destination mapping'}
  $children=if($target.PSIsContainer){@(Get-ChildItem -LiteralPath $resolved -Recurse -Force)}else{@($target)}
  foreach($child in $children){if($child.Attributes -band [IO.FileAttributes]::ReparsePoint){throw 'Reparse child'}}
  $files=@($children | Where-Object {-not $_.PSIsContainer})
  foreach($file in $files){
   $archived=if($target.PSIsContainer){Join-Path $destination $file.FullName.Substring($resolved.Length+1)}else{$destination}
   if(-not(Test-Path -LiteralPath $archived -PathType Leaf) -or (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash -ne (Get-FileHash -LiteralPath $archived -Algorithm SHA256).Hash){throw ('Unarchived bytes: '+$file.FullName)}
   $fileCount++;$byteCount+=$file.Length
  }
  if($target.PSIsContainer){$directoryCount+=1+@($children|Where-Object PSIsContainer).Count}
  $items+=@{caseNumber=$number;path=$resolved;archive=$destination;files=$files.Count}
 }
}
if(-not $PreviewOnly){foreach($item in $items){$checked=[IO.Path]::GetFullPath($item.path);if(-not $checked.StartsWith($workRoot+'\')){throw 'Delete escaped scope'};Remove-Item -LiteralPath $checked -Recurse -Force}}
$report=@{status=if($PreviewOnly){'verified_preview_only'}else{'archived_deferred_scratch_cleaned'};publishedCommit=$PublishedCommit;cases=$numbers;filesRemoved=if($PreviewOnly){0}else{$fileCount};filesVerified=$fileCount;directoriesRemoved=if($PreviewOnly){0}else{$directoryCount};bytesVerified=$byteCount;targets=$items;preserved=@('all8 immutable formal review archives','case137 formal image','shared public base image/source caches/helpers','deferred progress records','all prior published cases')}
if(-not $PreviewOnly){[IO.File]::WriteAllText((Join-Path $workRoot 'case137_prior_cleanup.json'),($report|ConvertTo-Json -Depth 6)+[char]10,(New-Object Text.UTF8Encoding($false)))}
$report|ConvertTo-Json -Depth 6
