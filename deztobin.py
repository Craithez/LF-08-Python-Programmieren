def dez_bin(zahl):
    while zahl != 0:
        rest = zahl % 2
        zahl = zahl // 2
        ergebnis = rest + zahl
        str(rest)
        print(rest)
zahl = int(input("Bitte geben sie eine Ganzzahl ein!: "))
dez_bin(zahl)

