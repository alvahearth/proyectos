import math


n1 = int(input("Ingresa el primero numero: "))
n2 = int(input("Ingresa el segundo numero: "))
n3 = int(input("Ingresa el tercero numero: "))

numero_mayor = 0

if n1 > n2 and n1 > n3:
    numero_mayor = n1
    print(numero_mayor)
elif n3 > n1 and n3 > n2:
    numero_mayor = n3
    print(numero_mayor)
elif n2 > n1 and n2 > n3:    
    numero_mayor = n2
    print(numero_mayor)
