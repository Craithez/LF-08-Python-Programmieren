def berechne_maximalpuls(alter, gewicht, geschlecht):
    if geschlecht.lower() == "männlich":
        maximalpuls = 214 - 0.5 * alter - 0.11 * gewicht
    elif geschlecht.lower() == "weiblich":
        maximalpuls = 210 - 0.5 * alter - 0.11 * gewicht

    return maximalpuls

alter = 30       
gewicht = 70
geschlecht = "weiblich"  

# Aufrufen + berechnen
maximalpuls = berechne_maximalpuls(alter, gewicht, geschlecht)

# Ausgeben
print(f"Der Maximalpuls für eine {alter}-jährige {geschlecht} mit {gewicht} kg beträgt {maximalpuls:.2f} Schläge pro Minute.")

#    else:
#        raise ValueError("Geschlecht muss 'männlich' oder 'weiblich' sein.")