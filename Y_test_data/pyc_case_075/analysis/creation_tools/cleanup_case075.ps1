param([Parameter(Mandatory=$true)][string]$PublishedCommit)
$ErrorActionPreference='Stop'
if ($PublishedCommit -notmatch '^[0-9a-f]{40}$') { throw 'Invalid published commit' }
$workRoot=[System.IO.Path]::GetFullPath('E:\CLB_Swe-bench\_work\pyc_batch')
$caseRoot=[System.IO.Path]::GetFullPath('E:\CLB_Swe-bench\pyc-swebench\Y_test_data\pyc_case_075')
$map=@{
 'case074-deferral'='analysis/prior_candidate_reviews/case074'; 'case074_cleanup.json'='analysis/prior_candidate_reviews/case074/case074_cleanup.json'; 'case074_progress.md'='analysis/prior_candidate_reviews/case074_authority_progress.md'; 'cleanup074_scratch.ps1'='analysis/prior_candidate_reviews/case074/cleanup074_scratch.ps1';
 'case075-image-context'='evaluator/image'; 'case075-probe-base'='verification/probes/base'; 'case075-probe-gold'='verification/probes/gold'; 'case075-probe-collect'='verification/probes/collect'; 'case075-prototype-build'='verification/prototype-build'; 'case075-runtime-audit'='verification/prototype-runtime-audit';
 'case075_gold.diff'='patches/gold_patch.diff'; 'case075_test.diff'='patches/test_patch.diff'; 'case075_upstream_api.json'='analysis/creation_tools/case075_upstream_api.raw.json'; 'case075_collected_nodes.json'='analysis/source_material/official_collected_nodes.json'; 'case075_formula_scan.json'='analysis/source_material/case075_formula_scan.json'; 'case075_source_record.png'='analysis/source_material/case075_source_record.png'; 'case075_swe-bench_record.png'='analysis/source_material/case075_swe-bench_record.png';
 'case075_spec.json'='analysis/creation_tools/case075_spec.json'; 'case075-control-before.txt'='analysis/creation_tools/case075-control-before.txt'; 'case075-control-after.txt'='analysis/creation_tools/case075-control-after.txt'
}
$targets=@(Get-ChildItem -LiteralPath $workRoot | Where-Object { $_.Name -match '(074|075)' -and $_.Name -notin @('case075_cleanup.json','case075_progress.md') })
$filesRemoved=0; $dirsRemoved=0; $bytesRemoved=0
foreach ($target in $targets) {
 $resolved=[System.IO.Path]::GetFullPath($target.FullName)
 if (-not $resolved.StartsWith($workRoot+'\') -or ($target.Attributes -band [System.IO.FileAttributes]::ReparsePoint)) { throw 'Unsafe resolved cleanup target' }
 $destination=if($map.ContainsKey($target.Name)){ $map[$target.Name] }elseif($target.Name -match '^(?:.*075.*\.(?:mjs|py|ps1)|Dockerfile\.pygame075-local)$'){ 'analysis/creation_tools/'+$target.Name }else{ throw ('Unmapped target '+$target.Name) }
 $archivedRoot=[System.IO.Path]::GetFullPath((Join-Path $caseRoot $destination))
 if (-not $archivedRoot.StartsWith($caseRoot+'\')) { throw 'Unsafe archive path' }
 $files=if($target.PSIsContainer){ @(Get-ChildItem -LiteralPath $resolved -Recurse -File) }else{@($target)}
 foreach($file in $files) {
  if($file.Attributes -band [System.IO.FileAttributes]::ReparsePoint){throw 'Reparse source'}
  $archived=if($target.PSIsContainer){Join-Path $archivedRoot $file.FullName.Substring($resolved.Length+1)}else{$archivedRoot}
  if(-not(Test-Path -LiteralPath $archived -PathType Leaf) -or (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash -ne (Get-FileHash -LiteralPath $archived -Algorithm SHA256).Hash){throw ('Unarchived or changed target '+$file.FullName)}
  $filesRemoved++;$bytesRemoved+=$file.Length
 }
 if($target.PSIsContainer){$dirsRemoved+=1+@(Get-ChildItem -LiteralPath $resolved -Recurse -Directory).Count}
}
foreach($target in $targets){Remove-Item -LiteralPath $target.FullName -Recurse -Force}
$report=@{caseNumber='075';status='published_cleaned';publicationPerformed=$true;publishedCommit=$PublishedCommit;image='yutu0814/pyc-case-075-pygame:benchmark-v1';imageDigest='sha256:09531e41aa8f9ff6c8dfe158e64846c0c11ff89f568409e474c6be948578392b';filesRemoved=$filesRemoved;directoriesRemoved=$dirsRemoved;bytesRemoved=$bytesRemoved;targets=@($targets.Name);preserved=@('all formal images','shared pygame/Pillow/UltraJSON source caches','shared batch helpers','case075_cleanup.json','case075_progress.md');prior074='deferred; all original evidence retained in delivered075 analysis/prior_candidate_reviews'}
$report|ConvertTo-Json -Depth 5|Set-Content -LiteralPath (Join-Path $workRoot 'case075_cleanup.json') -Encoding utf8NoBOM
$report|ConvertTo-Json -Depth 5
