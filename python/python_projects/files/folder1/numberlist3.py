a = range( 1, 35)
b = range( 30, 55)
lista_a = list()
lista_b = list()

for i in a:
    lista_a.append(i)

for i in b:
    lista_b.append(i)

lista = list()

for n in b:
    if n in lista:
        continue
    else:
        lista.append(n)

for n in a:
    if n in lista:
        continue
    else:
        lista.append(n)

print(lista)