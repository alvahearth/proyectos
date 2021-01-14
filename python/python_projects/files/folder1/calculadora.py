import math


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


def raiz(a):
    return math.sqrt(a)


while True:
    print("¿Que quieres Hacer?")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- División")
    print("5.- Raíz cuadrada")
    print("6.- Salir")

    user = input("Elige una opción: ")

    if user == "1":
        user1 = input("Digita el primer numero: ")
        print("")
        try:
            num1 = int(user1)
        except:
            print("Solo números")
            continue
        user2 = input("Digita el segundo número: ")
        print("")
        try:
            num2 = int(user2)
        except:
            print("Solo números")
        print("Resultado:", suma(num1, num2))
        print("")

    elif user == "2":
        user1 = input("Digita el primer numero: ")
        print("")
        try:
            num1 = int(user1)
        except:
            print("Solo números")
            continue
        user2 = input("Digita el segundo número:")
        print("")
        try:
            num2 = int(user2)
        except:
            print("Solo números")
            continue
        print("Resultado:", resta(num1, num2))
        print("")

    elif user == "3":
        user1 = input("Digita el primer numero: ")
        print("")
        try:
            num1 = int(user1)
        except:
            print("Solo números")
            continue
        user2 = input("Digita el segundo número: ")
        print("")
        try:
            num2 = int(user2)
        except:
            print("Solo números")
            continue
        print("Resultado:", multiplicacion(num1, num2))
        print("")

    elif user == "4":
        user1 = input("Digita el primer numero: ")
        print("")
        try:
            num1 = int(user1)
        except:
            print("Solo números")
            continue
        user2 = input("Digita el segundo número")
        print("")
        try:
            num2 = int(user2)
        except:
            print("Solo números")
            continue
        print("Resultado:", division(num1, num2))
        print("")
    elif user == "5":
        user1 = input("Ingresa un número: ")
        print("")
        try:
            num1 = int(user1)
        except:
            print("Solo números")
            continue
        print("Resultado:", raiz(num1))
        print("")
    elif user == "6":
        break
    else:
        print("Invalido")
        continue

