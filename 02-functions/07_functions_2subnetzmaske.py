def ip_und_maske_in_binär(ip_adresse, subnetzmaske):
    def dezimal_zu_binär(adresse):
        return '.'.join(f"{int(octet):08b}" for octet in adresse.split('.')) 
    # Selbe Funktion wie in LF-05 bei der IPv4 zu IPv6 Aufgabe "https://github.com/Craithez/LF-05-Pyhton-Programmieren/blob/main/Basics/IPv4toIPv6.py"

    ip_binär = dezimal_zu_binär(ip_adresse)
    maske_binär = dezimal_zu_binär(subnetzmaske)
    
    return ip_binär, maske_binär

ip_adresse = "10.10.89.122"
subnetzmaske = "255.255.255.0"
ip_binär, maske_binär = ip_und_maske_in_binär(ip_adresse, subnetzmaske)
print(f"IP: {ip_adresse} Binary: {ip_binär}")
print(f"Subnetzmaske: {subnetzmaske} Binary: {maske_binär}") 