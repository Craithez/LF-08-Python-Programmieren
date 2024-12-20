Get-ADComputer -Filter * -Property * |
Select-Object @{Name="ComputerName";Expression={$_.Name}},
              @{Name="OS";Expression={$_.OperatingSystem}},
              @{Name="OSVersion";Expression={$_.OperatingSystemVersion}},
              @{Name="IP";Expression={$_.IPv4Address}} |
Export-CSV -Path "C:\Test\ADcomputerslist.csv" -NoTypeInformation -Encoding UTF8
