from datetime import datetime

def aktuelles_datum_und_zeit():
    # Aktuelles Datum und Zeit abrufen
    jetzt = datetime.now()
    
    # Formatieren des Datums und der Zeit
    formatiert = jetzt.strftime("%A, %d.%m.%Y – %H:%M:%S")
    
    # Ausgabe des formatierten Datums und Zeitstempels
    print(formatiert)

# Funktion aufrufen
aktuelles_datum_und_zeit()