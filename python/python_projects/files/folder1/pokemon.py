pikachu_vida = 100
pikachu_ataque = 25
charmander_vida = 100
charmander_ataque = 30
turno = 0
while pikachu_vida >= 0 or charmander_vida >= 0:
    if turno == 0:
        print("turno 1")
        print("vida de pikachu:", pikachu_vida)
        print("vida de charmander:", charmander_vida)
        print("pikachu ataca")
        charmander_vida = charmander_vida - pikachu_ataque
        print("charmander recibe :", pikachu_ataque, "de daño")
        print("*******************************")
        print("* la vida de charmander es:", charmander_vida)
        print("*******************************")
        turno = turno + 1
    elif turno == 1:
        print("turno 0")
        print("vida de pikachu", pikachu_vida)
        print("vida de charmander", charmander_vida)
        print("charmander ataca")
        pikachu_vida = pikachu_vida - charmander_ataque
        print("pikachu recibe: ", charmander_ataque, "de daño")
        print("******************************")
        print("* la vida de pikachu es:", pikachu_vida)
        print("******************************")
        turno = turno - 1

if charmander_vida <= pikachu_vida:
    print("pikachu ganó")
else:
    print("charmander ganó")
