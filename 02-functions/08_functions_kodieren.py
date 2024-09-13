import base64

def base64_kodieren(text):
    # Text in Bytes
    text_bytes = text.encode('utf-8')
    # BASE64 kodieren
    base64_bytes = base64.b64encode(text_bytes)
    # BASE64 Bytes String konvertieren
    base64_text = base64_bytes.decode('utf-8')
    return base64_text

text = "Python is fun!"
kodierter_text = base64_kodieren(text)
print(f"BASE64-kodierter Text: {kodierter_text}")