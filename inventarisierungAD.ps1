'Get-ADComputer -Filter * -Property * |
Select-Object @{Name="ComputerName";Expression={$_.Name}},
              @{Name="OS";Expression={$_.OperatingSystem}},
              @{Name="OSVersion";Expression={$_.OperatingSystemVersion}},
              @{Name="IP";Expression={$_.IPv4Address}},
              @{Name="IP";Expression={$_.IPv4Address}} |
Export-CSV -Path "C:\Test\ADcomputerslist.csv" -NoTypeInformation -Encoding UTF8
'

$ComputerListe = Get-ADComputer -filter * | Select-Object -ExpandProperty Name
foreach ($Computer in $ComputerListe) {
    if (!(Test-Connection -Cn $Computer -BufferSize 16 -Count 1 -ea 0 -quiet)) {
        Write-Host "Kann $Computer nicht erreichen, offline" -f red   #Deutsches Windows kennt auch kein rot :P
    } else {
        $Ausgabetabelle = @()
        try {
            $Bios = Get-WmiObject win32_bios -ComputerName $Computer -ErrorAction Stop
            $Prozessor = Get-WmiObject –class Win32_processor -ComputerName $Computer -ErrorAction Stop
            $ADDaten = get-adcomputer $Computer -properties Name, LastlogonDate, Betriebssystem, ipv4Address, Enabled, Beschreibung, DistinguishedName -ErrorAction Stop
            $Ram = "{0} GB" -f ((Get-WmiObject Win32_PhysicalMemory -ComputerName $Computer | Measure-Object Capacity -Sum).Sum / 1GB)
            $SystemInfo = gwmi win32_computersystem -ComputerName $Computer | select @{
                Name = "Typ"
                Expression = {
                    if (($_.pcsystemtype -eq '2')) {
                        'Laptop'
                    } else {
                        'Desktop oder anderes'
                    }
                }
            }, Hersteller, @{
                Name = "Modell"
                Expression = {
                    if (($_.model -eq "$null")) {
                        'Virtuell'
                    } else {
                        $_.model
                    }
                }
            }, Benutzername -ErrorAction Stop

            # Abfrage der Monitor-Seriennummern - Klappt nur bedingt.
            $Monitore = Get-WmiObject Win32_DesktopMonitor -ComputerName $Computer -ErrorAction Stop
            $MonitorSeriennummern = $Monitore | ForEach-Object { $_.SerialNumber }

            $DatenObjekt = New-Object PSObject -Property @{
                Seriennummer = $Bios.serialnumber
                Computername = $ADDaten.name
                IpAdresse = $ADDaten.ipv4Address
                Aktiviert = $ADDaten.Enabled
                Beschreibung = $ADDaten.Beschreibung
                Ou = $ADDaten.DistinguishedName.split(',')[1].split('=')[1]
                Typ = $SystemInfo.typ
                Hersteller = $SystemInfo.Hersteller
                Modell = $SystemInfo.Modell
                RAM = $Ram
                ProzessorName = ($Prozessor.name | Out-String).Trim()
                AnzahlKerne = ($Prozessor.NumberOfCores | Out-String).Trim()
                AnzahlLogischeProzessoren = ($Prozessor.NumberOfLogicalProcessors | Out-String).Trim()
                Adressbreite = ($Prozessor.Addresswidth | Out-String).Trim()
                Betriebssystem = $ADDaten.Betriebssystem
                LetztesAnmeldedatum = $ADDaten.LastlogonDate
                AngemeldeterBenutzer = $SystemInfo.Benutzername
                MonitorSeriennummern = ($MonitorSeriennummern -join ", ")  # Alle Monitor-Seriennummern zusammenführen
            }
            $Ausgabetabelle += $DatenObjekt
        } catch [Exception] {
            "Fehler bei der Kommunikation mit $Computer, überspringe den nächsten"
        }

        $Ausgabetabelle | select Computername, Aktiviert, Beschreibung, IpAdresse, Ou, Typ, Seriennummer, Hersteller, Modell, RAM, ProzessorName, AnzahlKerne, AnzahlLogischeProzessoren, Adressbreite, Betriebssystem, AngemeldeterBenutzer, LetztesAnmeldedatum, MonitorSeriennummern | export-csv -Append c:\Test\NeuesADInventar.csv -nti
    }
}

#Notiz 
#Get-Module -ListAvailable ActiveDirectory
#Import-Module ActiveDirectory
#Und es funktioniert trotzdem nur im ISE.  ¯\_(ツ)_/¯ 
