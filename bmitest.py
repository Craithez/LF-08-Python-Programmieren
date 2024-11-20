def bmi_berechnen(gewicht, groesse, geschlecht):
    # Berechnung des BMI
    bmi = gewicht / (groesse ** 2)
    
    # Ausgabe des BMI
    print(f"Dein BMI ist: {bmi:.2f}")
    
    # Empfehlungen basierend auf BMI und Geschlecht
    if geschlecht.lower() == "frau":
        if bmi < 18.5:
            print("Du hast Untergewicht. Achte auf eine ausgewogene Ernährung.")
        elif 18.5 <= bmi < 24.9:
            print("Dein BMI ist im normalen Bereich. Weiter so!")
        elif 25 <= bmi < 29.9:
            print("Du hast Übergewicht. Versuche, dich gesünder zu ernähren und mehr zu bewegen.")
        else:
            print("Du hast Adipositas. Es wäre ratsam, einen Arzt zu konsultieren.")
    
    elif geschlecht.lower() == "mann":
        if bmi < 18.5:
            print("Du hast Untergewicht. Achte auf eine ausgewogene Ernährung.")
        elif 18.5 <= bmi < 24.9:
            print("Dein BMI ist im normalen Bereich. Weiter so!")
        elif 25 <= bmi < 29.9:
            print("Du hast Übergewicht. Versuche, dich gesünder zu ernähren und mehr zu bewegen.")
        else:
            print("Du hast Adipositas. Es wäre ratsam, einen Arzt zu konsultieren.")
    else:
        print("Ungültiges Geschlecht. Bitte gib 'frau' oder 'mann' ein.")
        
# Eingabewerte
gewicht = float(input("Gib dein Gewicht in kg ein: "))
groesse = float(input("Gib deine Größe in Metern ein (z.B. 1.75): "))
geschlecht = input("Gib dein Geschlecht ein (frau/mann): ")

bmi_berechnen(gewicht, groesse, geschlecht)
