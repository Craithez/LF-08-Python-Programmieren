import dht
import machine
import time

# Konfiguration des DHT22 Sensors an GPIO 15
sensor = dht.DHT22(machine.Pin(15))

while True:
    try:
        # Sensor lesen
        sensor.measure()
        
        # Temperatur und Luftfeuchtigkeit abrufen
        temperature = sensor.temperature()  # Temperatur in Celsius
        humidity = sensor.humidity()        # Luftfeuchtigkeit in %

        # Ausgabe der Werte
        print("Temperatur: {:.2f}°C, Luftfeuchtigkeit: {:.2f}%".format(temperature, humidity))

    except OSError as e:
        print("Fehler beim Auslesen des Sensors:", e)
    
    # Alle 20 Sekunden die Werte auslesen
    time.sleep(20)



import ssd1306

# Konfiguration des DHT22 Sensors an GPIO 15
sensor = dht.DHT22(machine.Pin(15))

# Konfiguration des I2C-Displays
i2c = machine.I2C(scl=machine.Pin(14), sda=machine.Pin(15), freq=200000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # 128x64 Pixel Display

# Display initialisieren
oled.fill(0)  # Display löschen
oled.text("DHT22 Daten", 0, 0)  # Titel
oled.show()

while True:
    try:
        # Sensor messen
        sensor.measure()
        
        # Temperatur und Luftfeuchtigkeit abrufen
        temperature = sensor.temperature()  # Temperatur in Celsius
        humidity = sensor.humidity()        # Luftfeuchtigkeit in %

        # Display löschen und neue Daten anzeigen
        oled.fill(0)  # Display löschen
        oled.text("DHT22 Daten", 0, 0)  # Titel
        oled.text("Temperatur: {:.2f}C".format(temperature), 0, 20)
        oled.text("Luftfeuchte: {:.2f}%".format(humidity), 0, 40)
        oled.show()

    except OSError as e:
        oled.fill(0)  # Display löschen
        oled.text("Fehler beim", 0, 0)
        oled.text("Auslesen des Sensors", 0, 20)
        oled.show()

    # Alle 2 Sekunden die Werte auslesen
    time.sleep(2)


