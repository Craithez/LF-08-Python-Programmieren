def bmi_berechnen(gewicht, groesse):
    # Berechnung des BMI
    bmi = gewicht / (groesse ** 2)
    # Ausgabe des BMI
    return bmi

# Eingabewerte
gewicht = float(input("Gib dein Gewicht in kg ein: "))
groesse = float(input("Gib deine Größe in Metern ein (z.B. 1.75): "))
bmi = bmi_berechnen(gewicht, groesse)
print(f"BMi: {bmi:.2f}")
