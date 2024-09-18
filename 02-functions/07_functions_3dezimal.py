def cidr_zu_dezimal(cidr_suffix):
    if not (0 <= cidr_suffix <= 32):
        raise ValueError("CIDR-Suffix muss zwischen 0 und 32 liegen.")
    
    # Netzmaske in binär Form, kenne keine bessere Methode. Also erst CIDR zu Binär, anschließend in Dezimal.
    # zfill ist straight von w3schools geklaut.
    # binär_maske 0:8, 8:16, 16:24 und 24:32. 
    binär_maske = (cidr_suffix * '1' + (32 - cidr_suffix) * '0').zfill(32)
    # Binär Maske in 8 Bit Blöcke für Dezimal anzuzeigen.
    # Binärblöcke in umwandeln.
    # range -> Start bei 0, Ende bei 32, Schritte 8.
    dezimal_blöcke = [str(int(binär_maske[i:i+8], 2)) for i in range(0, 32, 8)]
    
    return '.'.join(dezimal_blöcke)

# Selbes Spiel wie bei der "ersten" Aufgabe. Zahl muss im Rahmen bleiben.
cidr_suffix = 24
dezimal_maske = cidr_zu_dezimal(cidr_suffix)
print(f"CIDR-Suffix: {cidr_suffix} -> Dezimal: {dezimal_maske}")