import random

def number(x):
    intentos = 4
    random_number = random.randint(1,20)
    while x != random_number:
        print("Te quedan " + str(intentos) + " intentos")
        if intentos <= 0:
            print("Perdiste")
            break
        if x < random_number:
            print("El número es mayor")
            intentos -= 1
        else:
            print("El número es menor")
            intentos -= 1
        x = int(input("Ingresa otro número: "))
    if x == random_number:
        print("Ganaste")


if __name__ == "__main__":
    while True:
        print("""
        
        Trata de adivinar el número que escogio el computador
        
        te quedan 5 intentos
        
        Escribe "salir" para salir del programa
        
        """)
        user_input = input("Ingresa un número: ")
        if user_input == "salir":
            break
        try:
            numero = int(user_input)
        except:
            print("Ese no es un numero")
        
        x = number(numero)