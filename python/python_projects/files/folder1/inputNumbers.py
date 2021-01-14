numero_mayor = 0
numero_menor = None
final = 0
count = 0

while True:
    usp = input("Enter a number: ")

    if usp == "done":
        print("listo")
        break
    try:
        numero = int(usp)
    except:
        print("bad input")
        continue

    if numero > numero_mayor:
        numero_mayor = numero

    if numero_menor is None:
        numero_menor = numero
        if numero < numero_menor:
            numero = numero_menor

    print(numero)
    final = final + numero
    count = count + 1

print("there are", count, "numbers")
print("sum number is:", final)
print("max number is:", numero_mayor)
print("min number is:", numero_menor)
print("and the average is:", final / count)
