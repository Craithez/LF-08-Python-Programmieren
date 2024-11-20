import dht
import machine
import time
import ssd1306

# Potentiometer an GPIO32
potentiometer_pin = machine.Pin(32) 
# ADC für Potentiometer initialisieren
adc = machine.ADC(potentiometer_pin)  

# Konfiguration des DHT22 Sensors an GPIO 15
sensor = dht.DHT22(machine.Pin(15))

# Erster I2C-Bus für Display 1
i2c1 = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=200000)  
# Zweiter I2C-Bus für Display 2
i2c2 = machine.I2C(scl=machine.Pin(12), sda=machine.Pin(14), freq=200000) 

# Erstes SSD1306-Display DHT22-Daten
oled1 = ssd1306.SSD1306_I2C(128, 64, i2c1)  # 128x64 Pixel Display
# Zweites SSD1306-Display Potentiometer-Daten
oled2 = ssd1306.SSD1306_I2C(128, 64, i2c2)  # 128x64 Pixel Display

# Displays initialisieren
# Display 1 löschen
oled1.fill(0)  
#Titel
oled1.text("DHT22 Daten", 0, 0)  
oled1.show()

# Display 2 löschen
oled2.fill(0)  
#Titel
oled2.text("Potentiometer", 0, 0)   
oled2.show()

while True:
    try:
        # DHT22 Sensor messen
        sensor.measure()

        # Temperatur und Luftfeuchtigkeit abrufen
        temperature = sensor.temperature()  # Temperatur in Celsius
        humidity = sensor.humidity()        # Luftfeuchtigkeit in %

        # Potentiometerwert auslesen
        pot_value = adc.read()  # Wert des Potentiometers (zwischen 0 und 4095)
        pot_percent = (pot_value / 4095) * 100  # Umrechnung auf Prozentwert

        # Display für DHT22-Daten aktualisieren
        oled1.fill(0)  # Display löschen
        oled1.text("DHT22 Daten", 0, 0)  # Titel
        oled1.text("Temperatur: {:.2f}C".format(temperature), 0, 20)
        oled1.text("Luftfeuchte: {:.2f}%".format(humidity), 0, 40)
        oled1.show()

        # Display für Potentiometer-Daten aktualisieren
        oled2.fill(0)  # Display löschen
        oled2.text("Potentiometer", 0, 0)  # Titel
        oled2.text("Wert: {:.2f}%".format(pot_percent), 0, 20)  # Potentiometer-Wert als Prozent anzeigen
        oled2.show()

    except OSError as e:
        # Fehlerbehandlung bei Problemen mit dem Sensor
        print("Fehler beim Auslesen des Sensors:", e)
        oled1.fill(0)  # Display löschen
        oled1.text("Fehler beim", 0, 0)
        oled1.text("Auslesen des Sensors", 0, 20)
        oled1.show()

    # Alle 2 Sekunden die Werte auslesen
    time.sleep(2)
