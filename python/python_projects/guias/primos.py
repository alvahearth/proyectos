def primos(x):
    if  x == 1:
        return False
    contador = 0
    for i in range(1,x+1):
        if x % i == 0:
            contador = contador + 1
    if contador > 2:
        return False
    else:
        return True
    

if __name__ == "__main__":
    numero = int(input("Ingresa un número: "))
    if primos(numero):
        print("es primo")
    else:
        print("no es primo")