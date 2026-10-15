param([Parameter(Mandatory=$true)][string]$PublishedCommit)
$ErrorActionPreference='Stop'
if ($PublishedCommit -notmatch '^[0-9a-f]{40}$') { throw 'Invalid commit' }
$workRoot=[System.IO.Path]::GetFullPath('E:\CLB_Swe-bench\_work\pyc_batch')
$caseRoot=[System.IO.Path]::GetFullPath('E:\CLB_Swe-bench\pyc-swebench\Y_test_data\pyc_case_081')
$actualHead=git -C 'E:\CLB_Swe-bench\pyc-swebench' rev-parse HEAD
if ($LASTEXITCODE -ne 0 -or $actualHead.Trim() -ne $PublishedCommit) { throw 'Commit differs' }
$map=@{
 'case078-deferral'='analysis/prior_candidate_reviews/case078'
 'case078_progress.md'='analysis/prior_candidate_reviews/case078_authority_progress.md'
 'case078_cleanup.json'='analysis/prior_candidate_reviews/case078/case078_cleanup.json'
 'case081-image-context'='evaluator/image'
 'case081-probe-base'='verification/exploratory/base-build-only'
 'case081-probe-gold'='verification/exploratory/gold-build-only'
 'case081-probe-base-v2'='verification/probes/base'
 'case081-probe-gold-v2'='verification/probes/gold'
 'case081-probe-collect'='verification/probes/collect'
 'case081-runtime-audit'='verification/exploratory/runtime-before-default-font'
 'case081-runtime-audit-v2'='verification/prototype-runtime-audit'
 'case081-prototype-build'='verification/exploratory/prototype-build-only-v1'
 'case081-prototype-build-v2'='verification/exploratory/resource-build-daemon-eof'
 'case081-prototype-build-v3'='verification/prototype-build'
 'case081_gold.diff'='patches/gold_patch.diff'
 'case081_test.diff'='patches/test_patch.diff'
 'case081_upstream_api.json'='analysis/creation_tools/case081_upstream_api.raw.json'
 'case081_collected_nodes.json'='analysis/source_material/official_collected_nodes.json'
 'case081_formula_scan.json'='analysis/source_material/case081_formula_scan.json'
 'case081_source_record.png'='analysis/source_material/case081_source_record.png'
 'case081_swe-bench_record.png'='analysis/source_material/case081_swe-bench_record.png'
 'case081_spec.json'='analysis/creation_tools/case081_spec.json'
 'case081-control-before.txt'='analysis/creation_tools/case081-control-before.txt'
 'case081-control-after.txt'='analysis/creation_tools/case081-control-after.txt'
}
$targets=@(Get-ChildItem -LiteralPath $workRoot | Where-Object {
 ($_.Name -match '081' -or $_.Name -in @('case078-deferral','case078_progress.md','case078_cleanup.json')) -and $_.Name -notin @('case081_cleanup.json','case081_progress.md')
})
$filesRemoved=0; $dirsRemoved=0; $bytesRemoved=0
foreach ($target in $targets) {
 $resolved=[System.IO.Path]::GetFullPath($target.FullName)
 if (-not $resolved.StartsWith($workRoot+'\') -or ($target.Attributes -band [System.IO.FileAttributes]::ReparsePoint)) { throw 'Unsafe target' }
 $destination=if($map.ContainsKey($target.Name)){$map[$target.Name]}elseif($target.Name -match '081.*\.(mjs|py|ps1)$' -or $target.Name -match '^Dockerfile\.pygame081-'){ 'analysis/creation_tools/'+$target.Name }else{throw ('Unmapped '+$target.Name)}
 $archivedRoot=[System.IO.Path]::GetFullPath((Join-Path $caseRoot $destination))
 if(-not $archivedRoot.StartsWith($caseRoot+'\')){throw 'Unsafe archive path'}
 $files=if($target.PSIsContainer){@(Get-ChildItem -LiteralPath $resolved -Recurse -File)}else{@($target)}
 foreach($file in $files){
  if($file.Attributes -band [System.IO.FileAttributes]::ReparsePoint){throw 'Reparse source'}
  $archived=if($target.PSIsContainer){Join-Path $archivedRoot $file.FullName.Substring($resolved.Length+1)}else{$archivedRoot}
  if(-not(Test-Path -LiteralPath $archived -PathType Leaf) -or (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash -ne (Get-FileHash -LiteralPath $archived -Algorithm SHA256).Hash){throw ('Unarchived bytes: '+$file.FullName)}
  $filesRemoved++;$bytesRemoved+=$file.Length
 }
 if($target.PSIsContainer){$dirsRemoved+=1+@(Get-ChildItem -LiteralPath $resolved -Recurse -Directory).Count}
}
foreach($target in $targets){Remove-Item -LiteralPath $target.FullName -Recurse -Force}
$report=@{caseNumber='081';status='published_cleaned';publicationPerformed=$true;publishedCommit=$PublishedCommit;image='yutu0814/pyc-case-081-pygame:benchmark-v1';imageDigest='sha256:4e5d69e396505fea954f28acb59dc90ef522bafab05dd484c0299e628f938720';filesRemoved=$filesRemoved;directoriesRemoved=$dirsRemoved;bytesRemoved=$bytesRemoved;targets=@($targets.Name);preserved=@('formal images','shared source caches and batch helpers','earlier published cases','case081_cleanup.json','case081_progress.md')}
$report|ConvertTo-Json -Depth 5|Set-Content -LiteralPath (Join-Path $workRoot 'case081_cleanup.json') -Encoding utf8NoBOM
$report|ConvertTo-Json -Depth 5
