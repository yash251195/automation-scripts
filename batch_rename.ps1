<#
.SYNOPSIS
    Batch-rename a folder of files to a padded, sortable pattern.

.DESCRIPTION
    Turns junk like IMG_8842.jpg, scan001.pdf, export(3).csv into
    product_001.jpg, product_002.pdf, etc. Run with -WhatIf first to see the
    renames before anything actually changes on disk.

.EXAMPLE
    .\batch_rename.ps1 -Folder ".\photos" -Prefix "product" -WhatIf
    .\batch_rename.ps1 -Folder ".\photos" -Prefix "product"
#>

param(
    [Parameter(Mandatory = $true)]
    [string]$Folder,

    [string]$Prefix = "file",

    [string]$Extension = "*",

    [switch]$WhatIf
)

if (-not (Test-Path $Folder)) {
    Write-Error "Folder not found: $Folder"
    exit 1
}

$files = Get-ChildItem -Path $Folder -File -Filter "*.$Extension" | Sort-Object Name
if ($files.Count -eq 0) {
    Write-Host "No matching files."
    exit 0
}

$pad = ([string]$files.Count).Length
$i = 1
foreach ($f in $files) {
    $num = ([string]$i).PadLeft($pad, "0")
    $newName = "{0}_{1}{2}" -f $Prefix, $num, $f.Extension
    if ($WhatIf) {
        Write-Host "WOULD RENAME: $($f.Name)  ->  $newName"
    } else {
        Rename-Item -Path $f.FullName -NewName $newName
        Write-Host "renamed: $($f.Name)  ->  $newName"
    }
    $i++
}
