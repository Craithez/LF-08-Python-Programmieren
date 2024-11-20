def dezimal_zu_binaer(dezimalzahl):
    binärzahl = []
    if dezimalzahl == 0:
        print("0")
    while dezimalzahl != 0:
        bit = dezimalzahl % 2
        binärzahl.append(bit)
        reversed(binärzahl)
        dezimalzahl = dezimalzahl // 2
    else:
        print("Die Binärzahl ist: ", binärzahl)

dezimalzahl = int(input("Bitte geben sie eine Ganzzahl ein!:"))
dezimal_zu_binaer(dezimalzahl)
#binaer_reversed = dezimal_zu_binaer_reversed(dezimalzahl)
#print("Binär (umgekehrte Reihenfolge):", binaer_reversed)
