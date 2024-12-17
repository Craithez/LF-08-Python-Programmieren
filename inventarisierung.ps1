function Inventar {
    $zeit = Get-Date -Format "yyyyddMM_HHmmss"
    # Ordnerpfad mit den Inventar-CSV-Dateien
    $csvPfad = Read-Host "Gesamten Pfad angeben!"
    # Speicherort der finalen Inventardatei
    $outputPfad = Read-Host "Ganzen Pfad angeben, wohin wird kopiert?"
    # Teste mit einzigartigen Reihen
    $einzigReihe = Q{}
    
    # Loop für CSV Datei
    Get-ChildItem -Path $csv
}