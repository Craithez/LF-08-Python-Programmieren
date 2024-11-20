def prim_check (zahl):
    prim = True
    if zahl == 1:
        prim = False
    else:
        i=2
        while i <= zahl - 1:
            if zahl % i == 0:
                prim = False
            i += 1
    if prim:
        print(zahl, "ist eine Primzahl!")
    else:
        print(zahl, "ist keine Primzahl!")

zahl = int(input("Bitte Zahl eingeben: "))
prim_check(zahl)