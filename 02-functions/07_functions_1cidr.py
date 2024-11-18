def anzahl_hosts(cidr_suffix):
 #   if not (0 <= cidr_suffix <= 32):
 #       raise ValueError("CIDR-Suffix muss zwischen 0 und 32 liegen.")

    # Host-Bits 32
    host_bits = 32 - cidr_suffix
    # Anzahl der möglichen Hosts
    anzahl_hosts = (2 ** host_bits) - 2  # Abzug der Netzwerk- und Broadcast-Adresse
    #oder (host_bits ** 2) - 2
    
    return anzahl_hosts    # Oder mit print und dann unten aufrufen mit anzahl_hosts(6)
# Einfach Zahl ändern. Max sollte bekannt sein, alles über 31 produziert "falsche" Ergebnisse.
print(anzahl_hosts(6))