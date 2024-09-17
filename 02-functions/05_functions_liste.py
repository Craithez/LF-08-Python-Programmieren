def addiere_listen(liste1, liste2):
    if len(liste1) != 3 or len(liste2) != 3:
        raise ValueError("Beide Listen müssen genau drei Elemente enthalten.")
    
    # Liste + Liste
    ergebnis = [a + b for a, b in zip(liste1, liste2)]
    
    return ergebnis

liste1 = [1, 4, 7]
liste2 = [2, 3, 1]

resultat = addiere_listen(liste1, liste2)
print(resultat)  
