# Marc Lo Verde, LAV

$Datum = (Get-Date -Format d.M.yyyy__H_mm_s) 
# Bodenlos das ich das Datum nicht mit Leeschritt angeben kann aber egal.
If ((Test-Path -Path C:\Backups\GPO-Backup)) {
    If (Get-Module -ListAvailable -Name GroupPolicy) {
        New-Item -Path "C:\Backups\GPO-Backup\$Datum" -ItemType directory
        Backup-GPO -All -Path "C:\Backups\GPO-Backup\$Datum"
    }
    
    Else {
        Write-Warning "Fehler!"
    }
}
