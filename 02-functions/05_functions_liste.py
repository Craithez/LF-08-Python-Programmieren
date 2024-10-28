def addiere_listen(liste1, liste2):
    # Liste + Liste
    ergebnis = [a + b for a, b in zip(liste1, liste2)]
    
    return ergebnis


liste1 = [1, 4, 7]
liste2 = [2, 3, 1]

resultat = addiere_listen(liste1, liste2)
print(resultat)  



# Lösung Fabian
# def liste3(liste1,liste2):
#   ergebnis = []
# for i in range(3):
#   ergebnis.append(liste1[i] + liste2[i])
# return ergebnis
#... etc.


