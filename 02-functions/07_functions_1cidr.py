def anzahl_hosts(cidr_suffix):
    if not (0 <= cidr_suffix <= 32):
        raise ValueError("CIDR-Suffix muss zwischen 0 und 32 liegen.")
    
    # Host-Bits ist 32 
    host_bits = 32 - cidr_suffix
    # Möglichen Hosts
    anzahl_hosts = (2 ** host_bits) - 2  # Abzug der Netzwerk- und Broadcast-Adresse
    
    return anzahl_hosts

# Einfach Zahl ändern. Max sollte bekannt sein, alles über 31 produziert "falsche" Ergebnisse.
print(anzahl_hosts(29))  