salud = 100
ataque = 20
defensa = 35
espiritu = 20
magia = 68


def stats():
    print("Salud:", salud)
    print("Ataque:", ataque)
    print("Defensa:", defensa)
    print("Espiritu:", espiritu)
    print("Magia:", magia)


magia = magia + 20

stats()

print("")
print("asdaspdkasñdkasldasdkaslñdñasldkñaslkdñlasdkñlaskdñlasklas")
print("")

salud = salud + 20
stats()

fight = input("push a number :")
if fight == "5":
    stats()
elif fight == "8":
    print("hola?")
