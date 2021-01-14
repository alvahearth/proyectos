user_input = int(input("Ingresa un número: "))
user_range_end = int(input("Hasta que número quieres llegar: "))
x = range(1,user_range_end)
lista = list()

for n in x:
    if user_input % n == 0:
        lista.append(n)
    else:
        continue

print(lista)