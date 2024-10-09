# Sammelt alle GPo's.

Get-GPO -All | Backup-GPO -Path C:\Daten\GPOBackups\$(get-date -format 'HH:mm:ss dd-MM-yyyy')

