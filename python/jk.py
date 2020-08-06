# BASE STATS
health = 100
strength = 100
magic = 100
defense = 100

# BASE ATTACKS
slash = 70
kick = 50
punch = 30


def dañoCalculo(x):
    if x == 1:
        return (slash * strength) / 150
    if x == 2:
        return (kick * strength) / 150
    if x == 3:
        return (punch * strength) / 150


user = input("Ingresa un número: ")
if user == "1":
    numero = int(user)
    damage = dañoCalculo(numero)
    print(int(damage))
elif user == "2":
    numero = int(user)
    damage = dañoCalculo(numero)
    print(int(damage))
elif user == "3":
    numero = int(user)
    damage = dañoCalculo(numero)
    print(int(damage))
