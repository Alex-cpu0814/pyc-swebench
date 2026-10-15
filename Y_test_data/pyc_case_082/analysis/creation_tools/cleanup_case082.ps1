param([Parameter(Mandatory=$true)][string]$PublishedCommit)
$ErrorActionPreference='Stop'
if ($PublishedCommit -notmatch '^[0-9a-f]{40}$') { throw 'Invalid commit' }
$workRoot=[IO.Path]::GetFullPath('E:\CLB_Swe-bench\_work\pyc_batch')
$caseRoot=[IO.Path]::GetFullPath('E:\CLB_Swe-bench\pyc-swebench\Y_test_data\pyc_case_082')
$actualHead=git -C 'E:\CLB_Swe-bench\pyc-swebench' rev-parse HEAD
if ($LASTEXITCODE -ne 0 -or $actualHead.Trim() -ne $PublishedCommit) { throw 'Commit differs' }
$map=@{
 'case082-image-context'='evaluator/image'
 'case082-probe-base'='verification/probes/base'
 'case082-probe-gold'='verification/probes/gold'
 'case082-probe-collect'='verification/probes/collect'
 'case082-runtime-audit'='verification/prototype-runtime-audit'
 'case082-prototype-build'='verification/prototype-build'
 'case082_gold.diff'='patches/gold_patch.diff'
 'case082_test.diff'='patches/test_patch.diff'
 'case082_upstream_api.json'='analysis/creation_tools/case082_upstream_api.raw.json'
 'case082_collected_nodes.json'='analysis/source_material/official_collected_nodes.json'
 'case082_formula_scan.json'='analysis/source_material/case082_formula_scan.json'
 'case082_source_record.png'='analysis/source_material/case082_source_record.png'
 'case082_swe-bench_record.png'='analysis/source_material/case082_swe-bench_record.png'
 'case082_spec.json'='analysis/creation_tools/case082_spec.json'
 'case082-control-before.txt'='analysis/creation_tools/case082-control-before.txt'
 'case082-control-after.txt'='analysis/creation_tools/case082-control-after.txt'
}
$targets=@(Get-ChildItem -LiteralPath $workRoot | Where-Object { $_.Name -match '082' -and $_.Name -notin @('case082_cleanup.json','case082_progress.md') })
$filesRemoved=0; $dirsRemoved=0; $bytesRemoved=0
foreach ($target in $targets) {
 $resolved=[IO.Path]::GetFullPath($target.FullName)
 if (-not $resolved.StartsWith($workRoot+'\') -or ($target.Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'Unsafe target' }
 $destination=if($map.ContainsKey($target.Name)){$map[$target.Name]}elseif($target.Name -match '082.*\.(mjs|py|ps1)$' -or $target.Name -match '^Dockerfile\.pygame082-'){ 'analysis/creation_tools/'+$target.Name }else{throw ('Unmapped '+$target.Name)}
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
$report=@{caseNumber='082';status='published_cleaned';publicationPerformed=$true;publishedCommit=$PublishedCommit;image='yutu0814/pyc-case-082-pygame:benchmark-v1';imageDigest='sha256:9b466d593d9252da3ccb18d5270b5e8b1dcc456daa31e67273e94d2d48c9256a';filesRemoved=$filesRemoved;directoriesRemoved=$dirsRemoved;bytesRemoved=$bytesRemoved;targets=@($targets.Name);preserved=@('formal images','shared source caches and batch helpers','earlier published cases','case082_cleanup.json','case082_progress.md')}
[IO.File]::WriteAllText((Join-Path $workRoot 'case082_cleanup.json'),($report|ConvertTo-Json -Depth 5)+[char]10,(New-Object Text.UTF8Encoding($false)))
$report|ConvertTo-Json -Depth 5
