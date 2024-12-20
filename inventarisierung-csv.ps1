# Pfade zu den xlsx-Dateien
$inputxlsxPath = "C:\Test\ComputerNamen.xlsx"
$outputxlsxPath = "C:\Test\AusgabeDaten.xlsx"

# Einlesen der Computernamen aus der xlsx-Datei
$computernamen = Import-Excel -Path $inputxlsxPath

# Initialisieren der Ausgabevariablen
$outputData = @()

# Schleife über jeden Computernamen
foreach ($computer in $computernamen) {
    $computerName = $computer.ComputerName

    try {
        $computerSystem = Get-CimInstance -ClassName Win32_ComputerSystem -ComputerName $computerName
        $os = Get-CimInstance -ClassName Win32_OperatingSystem -ComputerName $computerName
        $cpu = Get-CimInstance -ClassName Win32_Processor -ComputerName $computerName
        $disk = Get-CimInstance -ClassName Win32_LogicalDisk -ComputerName $computerName -Filter "DeviceID='C:'"
        $network = Get-CimInstance -ClassName Win32_NetworkAdapterConfiguration -ComputerName $computerName | Where-Object { $_.IPAddress -ne $null }
        $monitors = Get-CimInstance -Namespace root\wmi -ClassName WmiMonitorID -ComputerName $computerName
        $dockingStation = Get-CimInstance -ClassName Win32_PnPEntity -ComputerName $computerName | Where-Object { $_.Name -like "*Docking Station*" }
        
        foreach ($adapter in $network) {
            $outputData += [PSCustomObject]@{
                ComputerName   = $computerSystem.Name
                Betriebssystem = "$($os.Caption), Service Pack: $($os.ServicePackMajorVersion).$($os.ServicePackMinorVersion)"
                CPU            = $cpu.Name
                FestplatteC    = "Kapazität: $($disk.Size / 1GB -as [int])GB, Freier Speicher: $($disk.FreeSpace / 1GB -as [int])GB"
                IPAdresse      = $adapter.IPAddress[0]
                MACAdresse     = $adapter.MACAddress
                DNSServer      = ($adapter.DNSServerSearchOrder -join ', ')
            }

            if ($monitors) {
                foreach ($monitor in $monitors) {
                    $outputData[-1].MonitorHersteller = [System.Text.Encoding]::ASCII.GetString($monitor.Manufacturer) -replace '\x00'
                    $outputData[-1].MonitorName = [System.Text.Encoding]::ASCII.GetString($monitor.UserFriendlyName) -replace '\x00'
                    $outputData[-1].MonitorSeriennummer = [System.Text.Encoding]::ASCII.GetString($monitor.SerialNumberID) -replace '\x00'
                }
            }

            if ($dockingStation) {
                foreach ($dock in $dockingStation) {
                    $outputData[-1].DockingstationName = $dock.Name
                    $outputData[-1].DockingstationHersteller = $dock.Manufacturer
                    $outputData[-1].DockingstationMACAdresse = $dock.MACAddress
                    $outputData[-1].DockingstationSeriennummer = $dock.SerialNumber
                }
            }
        }
    } catch {
        Write-Warning "Fehler beim Zugriff auf $computerName $($_)"
    }
}

# Exportieren der gesammelten Daten in die Output xlsx-Datei
$outputData | Export-Excel -Path $outputxlsxPath -NoTypeInformation
