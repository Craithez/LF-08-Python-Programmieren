def addiere_listen(liste1, liste2):
    if len(liste1) != 3 or len(liste2) != 3:
        raise ValueError("Beide Listen müssen genau drei Elemente enthalten.")
    
    # "Addiere der beiden Listen"
    ergebnis = [a + b for a, b in zip(liste1, liste2)]
    
    return ergebnis

# Beispiel Listen
liste1 = [1, 4, 7]
liste2 = [2, 3, 1]

# Funktion aufrufen und Ergebnis ausgeben
resultat = addiere_listen(liste1, liste2)
print(resultat)  
# Gibt [3, 7, 8] aus