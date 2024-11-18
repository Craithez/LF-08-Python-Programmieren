def dez_bin(zahl):
    if zahl == 0:
        return "0"
    binärzahl = ""
    while zahl > 0:
        rest = zahl % 2
        binärzahl = str(rest) + (binärzahl)
        zahl = zahl // 2
    return binärzahl

def binärausgabe(binärzahl):
    print(f"Ausgabe:{binärzahl}")

zahl = int(input("Bitte geben sie eine Ganzzahl ein!:"))
binärzahl = dez_bin(zahl)
binärausgabe(binärzahl)
