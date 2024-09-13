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


# Aufgabe: Friday, 13.09.2024 – 13:27:15

# Weil ich mich selber hasse hier für deutsche Ausgabe:
""" from datetime import datetime

def aktuelles_datum_und_zeit():
    # Wochentage und Monate auf Deutsch
    wochen_tag = {
        'Monday': 'Montag', 'Tuesday': 'Dienstag', 'Wednesday': 'Mittwoch',
        'Thursday': 'Donnerstag', 'Friday': 'Freitag', 'Saturday': 'Samstag',
        'Sunday': 'Sonntag'
    }
    
    monate = {
        'January': 'Januar', 'February': 'Februar', 'March': 'März',
        'April': 'April', 'May': 'Mai', 'June': 'Juni',
        'July': 'Juli', 'August': 'August', 'September': 'September',
        'October': 'Oktober', 'November': 'November', 'December': 'Dezember'
    }

    # Aktuelles Datum und Zeit abrufen
    jetzt = datetime.now()
    
    # Englische Namen der Wochentage und Monate abrufen
    englischer_wochentag = jetzt.strftime("%A")
    englischer_monat = jetzt.strftime("%B")
    
    # Namen auf Deutsch übersetzen
    deutscher_wochentag = wochen_tag[englischer_wochentag]
    deutscher_monat = monate[englischer_monat]
    
    # Formatieren des Datums und der Zeit
    formatiert = jetzt.strftime(f"{deutscher_wochentag}, %d.{deutscher_monat}.%Y – %H:%M:%S")
    
    # Ausgabe des formatierten Datums und Zeitstempels
    print(formatiert) """

# Funktion aufrufen
# aktuelles_datum_und_zeit()