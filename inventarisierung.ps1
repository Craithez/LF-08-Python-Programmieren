$computerName = "LAV" 
$computerSystem = Get-WmiObject -Class Win32_ComputerSystem -ComputerName $computerName
$os = Get-WmiObject -Class Win32_OperatingSystem -ComputerName $computerName
$cpu = Get-WmiObject -Class Win32_Processor -ComputerName $computerName
$disk = Get-WmiObject -Class Win32_LogicalDisk -ComputerName $computerName -Filter "DeviceID='C:'"
$network = Get-WmiObject -Class Win32_NetworkAdapterConfiguration -ComputerName $computerName | Where-Object { $_.IPAddress -ne $null }
$software = Get-WmiObject -Class Win32_Product -ComputerName $computerName
$devices = Get-WmiObject -Class Win32_PnPEntity -ComputerName $computerName
$monitors = Get-WmiObject -Class Win32_DesktopMonitor -ComputerName $computerName
$dockingStation = Get-WmiObject -Class Win32_PnPEntity -ComputerName $computerName | Where-Object { $_.Name -like "*Docking Station*" }

$output = @()

$output += "Computer Name: $($computerSystem.Name)"
$output += "Betriebssystem: $($os.Caption), Service Pack: $($os.ServicePackMajorVersion).$($os.ServicePackMinorVersion)"
$output += "CPU: $($cpu.Name)"
$output += "Festplatte C: Kapazität: $($disk.Size / 1GB -as [int])GB, Freier Speicher: $($disk.FreeSpace / 1GB -as [int])GB"
$output += "Netzwerkinformationen: "
$network | ForEach-Object {
    $output += "`tIP-Adresse: $($_.IPAddress[0])"
    $output += "`tMAC-Adresse: $($_.MACAddress)"
    $output += "`tDNS-Server: $($_.DNSServerSearchOrder -join ', ')"
}
$output += "Installierte Software: "
$software | ForEach-Object {
    $output += "`t$($_.Name)"
}
$output += "Hardwaregeräte: "
$devices | ForEach-Object {
    $output += "`t$($_.Caption)"
}
$output += "Monitor-Informationen: "
$monitors | ForEach-Object {
    $output += "`tPNP-Geräte-ID: $($_.PNPDeviceID)"
    $output += "`tSeriennummer: $($_.SerialNumber)"
}
$output += "Dockingstation: "
$dockingStation | ForEach-Object {
    $output += "`tName: $($_.Name)"
    $output += "`tHersteller: $($_.Manufacturer)"
    $output += "`tSeriennummer: $($_.SerialNumber)"
}

$output | Out-File -FilePath "C:\Test\Datei.txt"
