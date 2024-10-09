$Today=Get-Date -Format "dd-MM-yyyy"

$Path="C:\Daten"
$Backup="$Path\GPOBackup"
$Report="$Path\GPOReport"

if (-not (Test-Path $Backup)) {
New-Item -Path $Backup -ItemType "directory"
}
if (-not (Test-Path $Report)) {
New-Item -Path $Report -ItemType "directory"
}

# Sammelt alle GPo's.
$AllGPOs=Get-GPO -All

foreach ($GPO in $AllGPOs) {
    $Name=$GPO.DisplayName
    if ($GPO.ModificationTime.Date -eq (Get-Date).Date){
    Backup-GPO -Name $Name -Path $Backup
    Get-GPOReport -Name $Name -Path $Report\$Name-$Today.xml -ReportType Xml
    }
}
(Get-ADOrganizationalUnit -filter * | Get-GPInheritance).GpoLinks | Select-Object -Property Target,DisplayName,Enabled,Enforced,Order | Export-Csv -Path "$Path\gPLink.csv"