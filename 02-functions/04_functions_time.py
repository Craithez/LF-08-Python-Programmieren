from datetime import datetime

def aktuelles_datum_und_zeit():
    jetzt = datetime.now()
    
    # Formatierung
    formatiert = jetzt.strftime("%A, %d.%m.%Y – %H:%M:%S")
    
    # Ausgabe
    print(formatiert)

# Aufrufen
aktuelles_datum_und_zeit()

# Weil ich mich selber hasse hier die deutsche Ausgabe:
""" from datetime import datetime

def aktuelles_datum_und_zeit():
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

    jetzt = datetime.now()
    
    englischer_wochentag = jetzt.strftime("%A")
    englischer_monat = jetzt.strftime("%B")
    
    deutscher_wochentag = wochen_tag[englischer_wochentag]
    deutscher_monat = monate[englischer_monat]
    
    formatiert = jetzt.strftime(f"{deutscher_wochentag}, %d.{deutscher_monat}.%Y – %H:%M:%S")
    
    print(formatiert) """
# aktuelles_datum_und_zeit()