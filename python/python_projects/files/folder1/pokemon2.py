turno = 0
# salud
pikachu_vida = 100
squirtle_vida = 100
# ataques pikachu
ataque1depikachu = "Impactrueno"
dañoat1pika = 30
ataque2depikachu = "Tacleada"
dañoat2pika = 25

# ataques squirtle
ataque1desquirtle = "Pistola de agua"
dañoat1squ = 30
ataque2desquirtle = "Viento helado"
dañoat2squ = 35

while pikachu_vida >= 0 or squirtle_vida >= 0:
    if turno == 0:
        print("----------------------------")
        print("Turno de Squirtle")
        print("Selecciona uno de los siguientes ataques:")
        print("1.- Pistola de agua = 30 Daño")
        print("2.- Viento helado = 35 Daño")

        movimientos_de_squirtle = input("Ingresa un numero: ")

        try:
            ataque1 = int(movimientos_de_squirtle)
            if ataque1 == 1:
                ataque1 = ataque1desquirtle
                daño1 = dañoat1squ
            elif ataque1 == 2:
                ataque1 = ataque2desquirtle
                daño1 = dañoat2squ
            elif ataque1 < 1 or ataque1 > 2:
                print("invalid")
        except:
            print("invalid")
            quit()

        print("squirtle utiliza:", ataque1)
        print("Pikachu recibe:", daño1, "de daño")
        pikachu_vida = pikachu_vida - daño1
        print("La salud de pikachu es:", pikachu_vida)
        print("La salud de Squirtle es:", squirtle_vida)
        turno = turno + 1

    elif turno == 1:
        print("----------------------------")
        print("Turno de pikachu")
        print("Selecciona uno de los siguientes ataques:")
        print("1.- Impactrueno = 30 Daño")
        print("2.- Tacleada = 25 Daño")

        movimientos_de_pikachu = input("Ingresa un numero: ")

        try:
            ataque2 = int(movimientos_de_pikachu)
            if ataque2 == 1:
                ataque2 = ataque1depikachu
                daño2 = dañoat1pika
            elif ataque2 == 2:
                ataque2 = ataque2depikachu
                daño2 = dañoat2pika
            elif ataque2 < 1 or ataque2 > 2:
                print("Invalid")
        except:
            print("Invalid")
            quit()

        print("Pikachu utiliza:", ataque2)
        print("Squirtle recibe:", daño2, "de daño")
        squirtle_vida = squirtle_vida - daño2
        print("La salude de pikachu es:", pikachu_vida)
        print("La salud de Squirtle es:", squirtle_vida)
        turno = turno - 1


if pikachu_vida > squirtle_vida:
    print("Ganó Pikachu")
else:
    print("Gano Squirtle")
