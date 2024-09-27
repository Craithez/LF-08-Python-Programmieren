print("Freitag, Samstag , Sonntag".replace(" ","").split(","))
wochenende = ("Freitag, Samstag, Sonntag")
lsg1 = wochenende.replace(" ", "").split(",")
print(lsg1)
wochenende2 = ["Freitag","Samstag","Sonntag"]
satz = ", ".join(wochenende2)
print(satz)
wochenende3 = ["Freitag","Samstag","Sonntag"]
str(wochenende3).split(", ")
print(wochenende3)
wochenende4 = ["Freitag","Samstag","Sonntag"]
stringliste = ""
for i in wochenende4:
    stringliste = stringliste+str(i)
print(stringliste)
wochenende5 = ["Freitag","Samstag","Sonntag"]
wochenende5 = wochenende5[0] + ", " + wochenende5[1] + ", "
print(wochenende5)