param([Parameter(Mandatory=$true)][string]$PublishedCommit)
$ErrorActionPreference='Stop'
if($PublishedCommit -notmatch '^[0-9a-f]{40}$'){throw 'Invalid commit'}
$workRoot=[IO.Path]::GetFullPath('E:\CLB_Swe-bench\_work\pyc_batch')
$repoRoot='E:\CLB_Swe-bench\pyc-swebench'
$caseRoot=[IO.Path]::GetFullPath((Join-Path $repoRoot 'Y_test_data\pyc_case_175'))
$actualHead=git -C $repoRoot rev-parse HEAD
if($LASTEXITCODE -ne 0 -or $actualHead.Trim() -ne $PublishedCommit){throw 'Commit differs'}
$publication=Get-Content -LiteralPath (Join-Path $caseRoot 'verification\publication\publication.json') -Raw | ConvertFrom-Json
$map=@{
 'case175-image-context'='analysis/source_material/prototype-image-context'
 'case175-probe-base'='verification/probes/base'
 'case175-probe-gold'='verification/probes/gold'
 'case175-probe-collect'='verification/probes/collect'
 'case175-prototype-build'='verification/history/case175-prototype-build'
 'case175-runtime-audit'='verification/prototype-runtime-audit'
 'case175_gold.diff'='patches/gold_patch.diff'
 'case175_test.diff'='patches/test_patch.diff'
 'case175_source_record.png'='analysis/source_material/case175_source_record.png'
 'case175_swe-bench_record.png'='analysis/source_material/case175_swe-bench_record.png'
 'case175_formula_scan.json'='analysis/source_material/case175_formula_scan.json'
 'case175_pr187.raw.html'='analysis/source_material/case175_pr187.raw.html'
}
$targets=@(Get-ChildItem -LiteralPath $workRoot | Where-Object {$_.Name -match '175' -and $_.Name -notin @('case175_cleanup.json','case175_progress.md')})
$filesRemoved=0;$dirsRemoved=0;$bytesRemoved=0
foreach($target in $targets){
 $resolved=[IO.Path]::GetFullPath($target.FullName)
 if(-not $resolved.StartsWith($workRoot+'\') -or ($target.Attributes -band [IO.FileAttributes]::ReparsePoint)){throw 'Unsafe target'}
 $destination=if($map.ContainsKey($target.Name)){$map[$target.Name]}elseif($target.PSIsContainer){'verification/history/'+$target.Name}else{'analysis/creation_tools/'+$target.Name}
 $archivedRoot=[IO.Path]::GetFullPath((Join-Path $caseRoot $destination))
 if(-not $archivedRoot.StartsWith($caseRoot+'\')){throw 'Unsafe archive path'}
 $files=if($target.PSIsContainer){@(Get-ChildItem -LiteralPath $resolved -Recurse -File)}else{@($target)}
 foreach($file in $files){
  if($file.Attributes -band [IO.FileAttributes]::ReparsePoint){throw 'Reparse source'}
  $archived=if($target.PSIsContainer){Join-Path $archivedRoot $file.FullName.Substring($resolved.Length+1)}else{$archivedRoot}
  if(-not(Test-Path -LiteralPath $archived -PathType Leaf) -or (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash -ne (Get-FileHash -LiteralPath $archived -Algorithm SHA256).Hash){throw ('Unarchived bytes: '+$file.FullName)}
  $filesRemoved++;$bytesRemoved+=$file.Length
 }
 if($target.PSIsContainer){$dirsRemoved+=1+@(Get-ChildItem -LiteralPath $resolved -Recurse -Directory).Count}
}
foreach($target in $targets){Remove-Item -LiteralPath $target.FullName -Recurse -Force}
$report=@{caseNumber='175';status='published_cleaned';publicationPerformed=$true;publishedCommit=$PublishedCommit;image=$publication.image;imageDigest=$publication.registry_digest;filesRemoved=$filesRemoved;directoriesRemoved=$dirsRemoved;bytesRemoved=$bytesRemoved;targets=@($targets.Name);preserved=@('formal images','shared source caches and batch helpers','earlier published cases','case175_cleanup.json','case175_progress.md')}
[IO.File]::WriteAllText((Join-Path $workRoot 'case175_cleanup.json'),($report|ConvertTo-Json -Depth 5)+[char]10,(New-Object Text.UTF8Encoding($false)))
$report|ConvertTo-Json -Depth 5
