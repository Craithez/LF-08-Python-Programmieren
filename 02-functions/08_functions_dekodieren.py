import base64

def base64_dekodieren(base64_text):
    # BASE64 Text in Bytes
    base64_bytes = base64_text.encode('utf-8')
    # BASE64 dekodieren
    text_bytes = base64.b64decode(base64_bytes)
    # Bytes in String konvertieren
    text = text_bytes.decode('utf-8')
    print(f"Dekodierter Text: {text}")
# Hatte Alt+F4 erwartet.
kodierter_text = "Q1RSTCtBTFQrREVM"
base64_dekodieren(kodierter_text)
