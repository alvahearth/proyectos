a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a)
user_number = int(input("Ingresa un número: "))

lista = list()
for n in a:
    if n < user_number:
        lista.append(n)

print(lista)