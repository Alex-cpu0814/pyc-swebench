param([Parameter(Mandatory=$true)][string]$PublishedCommit)
$ErrorActionPreference='Stop'
if ($PublishedCommit -notmatch '^[0-9a-f]{40}$') { throw 'Invalid commit' }
$workRoot=[IO.Path]::GetFullPath('E:\CLB_Swe-bench\_work\pyc_batch')
$caseRoot=[IO.Path]::GetFullPath('E:\CLB_Swe-bench\pyc-swebench\Y_test_data\pyc_case_086')
$actualHead=git -C 'E:\CLB_Swe-bench\pyc-swebench' rev-parse HEAD
if ($LASTEXITCODE -ne 0 -or $actualHead.Trim() -ne $PublishedCommit) { throw 'Commit differs' }
$map=@{
 'case083-duplicate'='analysis/prior_candidate_reviews/case083'
 'case083_progress.md'='analysis/prior_candidate_reviews/case083_authority_progress.md'
 'review_case083_duplicate.mjs'='analysis/prior_candidate_reviews/case083/review_case083_duplicate.mjs'
 'case086_upstream_associated_prs.json'='analysis/source_material/upstream_associated_prs.json'
 'case086_upstream_pr_commits.json'='analysis/source_material/upstream_pr_commits.json'
 'case086-image-context'='evaluator/image'
 'case086-probe-base'='verification/probes/base'
 'case086-probe-gold'='verification/probes/gold'
 'case086-probe-collect'='verification/probes/collect'
 'case086-runtime-audit'='verification/prototype-runtime-audit'
 'case086-prototype-build'='verification/prototype-build'
 'case086_gold.diff'='patches/gold_patch.diff'
 'case086_test.diff'='patches/test_patch.diff'
 'case086_upstream_api.json'='analysis/creation_tools/case086_upstream_api.raw.json'
 'case086_collected_nodes.json'='analysis/source_material/official_collected_nodes.json'
 'case086_formula_scan.json'='analysis/source_material/case086_formula_scan.json'
 'case086_source_record.png'='analysis/source_material/case086_source_record.png'
 'case086_swe-bench_record.png'='analysis/source_material/case086_swe-bench_record.png'
 'case086_spec.json'='analysis/creation_tools/case086_spec.json'
 'case086-control-before.txt'='analysis/creation_tools/case086-control-before.txt'
 'case086-control-after.txt'='analysis/creation_tools/case086-control-after.txt'
}
$targets=@(Get-ChildItem -LiteralPath $workRoot | Where-Object { ($_.Name -match '086' -or $_.Name -in @('case083-duplicate','case083_progress.md','review_case083_duplicate.mjs')) -and $_.Name -notin @('case086_cleanup.json','case086_progress.md') })
$filesRemoved=0; $dirsRemoved=0; $bytesRemoved=0
foreach ($target in $targets) {
 $resolved=[IO.Path]::GetFullPath($target.FullName)
 if (-not $resolved.StartsWith($workRoot+'\') -or ($target.Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw 'Unsafe target' }
 $destination=if($map.ContainsKey($target.Name)){$map[$target.Name]}elseif($target.Name -match '086.*\.(mjs|py|ps1)$' -or $target.Name -match '^Dockerfile\.pygame086-'){ 'analysis/creation_tools/'+$target.Name }else{throw ('Unmapped '+$target.Name)}
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
$report=@{caseNumber='086';status='published_cleaned';publicationPerformed=$true;publishedCommit=$PublishedCommit;image='yutu0814/pyc-case-086-pygame:benchmark-v1';imageDigest='sha256:11e605344ed4675be7b010289e782843d09aa9efc3fae6d819d905c65ab7a0f3';filesRemoved=$filesRemoved;directoriesRemoved=$dirsRemoved;bytesRemoved=$bytesRemoved;targets=@($targets.Name);preserved=@('formal images','shared source caches and batch helpers','earlier published cases','case086_cleanup.json','case086_progress.md')}
[IO.File]::WriteAllText((Join-Path $workRoot 'case086_cleanup.json'),($report|ConvertTo-Json -Depth 5)+[char]10,(New-Object Text.UTF8Encoding($false)))
$report|ConvertTo-Json -Depth 5
