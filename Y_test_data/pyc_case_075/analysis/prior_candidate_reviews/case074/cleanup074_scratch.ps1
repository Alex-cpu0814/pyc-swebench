$ErrorActionPreference = 'Stop'
$workRoot = [System.IO.Path]::GetFullPath('E:\CLB_Swe-bench\_work\pyc_batch')
$archiveRoot = Join-Path $workRoot 'case074-deferral'
$targets = @(Get-ChildItem -LiteralPath $workRoot | Where-Object { $_.Name -match '^(case074|Dockerfile\.pygame074|initialize_case074|stage_case074|audit_case074|build_case074|defer_case074)' -and $_.Name -notin @('case074-deferral','case074_progress.md','case074_cleanup.json') })
$totalFiles = 0; $totalDirectories = 0; $totalBytes = 0
foreach ($target in $targets) {
    $resolvedTarget = [System.IO.Path]::GetFullPath($target.FullName)
    if (-not $resolvedTarget.StartsWith($workRoot + '\') -or ($target.Attributes -band [System.IO.FileAttributes]::ReparsePoint)) { throw 'Unsafe target' }
    $files = if ($target.PSIsContainer) { @(Get-ChildItem -LiteralPath $resolvedTarget -Recurse -File) } else { @($target) }
    foreach ($file in $files) {
        if ($file.Attributes -band [System.IO.FileAttributes]::ReparsePoint) { throw 'Reparse file' }
        $relative = $file.FullName.Substring($workRoot.Length + 1)
        $archived = Join-Path $archiveRoot $relative
        if (-not (Test-Path -LiteralPath $archived -PathType Leaf) -or (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash -ne (Get-FileHash -LiteralPath $archived -Algorithm SHA256).Hash) { throw ('Archive mismatch: ' + $relative) }
        $totalFiles++; $totalBytes += $file.Length
    }
    if ($target.PSIsContainer) { $totalDirectories += 1 + @(Get-ChildItem -LiteralPath $resolvedTarget -Recurse -Directory).Count }
}
foreach ($target in $targets) { Remove-Item -LiteralPath $target.FullName -Recurse -Force }
$report = @{ caseNumber='074'; status='deferred_prototype_cleaned'; publicationPerformed=$false; removedPrototype='pyc-case074-prototype-base:latest'; filesRemoved=$totalFiles; directoriesRemoved=$totalDirectories; bytesRemoved=$totalBytes; evidencePreserved='case074-deferral'; preserved=@('shared pygame sourcecache','all formal images','case074_progress.md'); targets=@($targets.Name) }
$report | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $workRoot 'case074_cleanup.json') -Encoding utf8NoBOM
$report | ConvertTo-Json -Depth 5
