class Jaeger:
    def __init__(spielfigur, beweglichkeit, trefferwertung, hp):
        spielfigur.beweglichkeit = beweglichkeit
        spielfigur.trefferwertung = trefferwertung
        spielfigur.angriffskraft = beweglichkeit * 2
        spielfigur.mdj = 120
        spielfigur.hp = hp
    def aimedshot(spielfigur, schaden):
        if spielfigur.angriffskraft > 0:
            schaden = 1.5 * spielfigur.angriffskraft + spielfigur.mdj
            print(f"{schaden} wurde angerichtet!")
        else:
            print("Ende")
    def schadendrücken(spielfigur, schadendrücken):
        schadendrücken = spielfigur.angriffskraft + spielfigur.mdj
class subclass Gegner(spielfigur):
    def __init__(spielfigur, hp):
        spielfigur.hp = hp        
        def blocken(spielfigur, blocken):
        Gegner.blocken = blocken
        def schadenerhalten(spielfigur, schadenerhalten):
            


jaeger = Jaeger(beweglichkeit=500, trefferwertung=155, hp=100)
print(f"Beweglichkeit: {jaeger.beweglichkeit}, Angriffskraft {jaeger.angriffskraft+jaeger.mdj}, Trefferwertung: {jaeger.trefferwertung}, HP: {jaeger.hp}")
jaeger.aimedshot(3)


    
