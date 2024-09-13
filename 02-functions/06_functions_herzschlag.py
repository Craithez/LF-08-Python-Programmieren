def berechne_maximalpuls(alter, gewicht, geschlecht):
    if geschlecht.lower() == "männlich":
        maximalpuls = 214 - 0.5 * alter - 0.11 * gewicht
    elif geschlecht.lower() == "weiblich":
        maximalpuls = 210 - 0.5 * alter - 0.11 * gewicht
    else:
        raise ValueError("Geschlecht muss 'männlich' oder 'weiblich' sein.")
    
    return maximalpuls

# Beispielwerte
alter = 30       
gewicht = 70
geschlecht = "weiblich"  

# Funktion aufrufen und Ergebnis berechnen
maximalpuls = berechne_maximalpuls(alter, gewicht, geschlecht)

# Ergebnis ausgeben
print(f"Der Maximalpuls für eine {alter}-jährige {geschlecht} mit {gewicht} kg beträgt {maximalpuls:.2f} Schläge pro Minute.")