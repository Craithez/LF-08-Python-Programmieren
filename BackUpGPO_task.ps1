# Sammelt alle GPo's.
# Get-GPO -All | Backup-GPO -Path C:\Daten\GPOBackup

$GPOInfo = Get-GPO -All -Domain $domain -Server $Server
$Date = Get-Date -UFormat "%d-%m-%Y"
$UpdatedPath = "$path\$date"
New-item $UpdatedPath -ItemType directory | Out-Null

ForEach ($GPO in $GPOInfo) {

    #Assign temp variables for various parts of GPO data
    Write-Host "Backing up GPO named: " $GPO.Displayname
    $BackupInfo = Backup-GPO -Name $GPO.DisplayName -Domain $Domain  path $UpdatedPath -Server $Server
    $GpoBackupID = $BackupInfo.ID.Guid
    $GpoName = $BackupInfo.DisplayName
    $CurrentFolderName = $UpdatedPath + "\" + "{"+ $GpoBackupID + "}"
    $NewFolderName = $UpdatedPath + "\" + $GPOName

    #Rename the newly created GPO backup subfolder from its GPO ID to the GPO Displayname + GUID
    rename-item $CurrentFolderName -newname $NewFolderName
}