numero_menor = None
print("El mumero mas mas bajo a al comienzo es 0")
for value in [74,91,42,21,19,25]:
    if numero_menor is None:
        numero_menor = value
        print(numero_menor)
    elif numero_menor > value:
        numero_menor = value
        print(numero_menor)

print("el numero menor es:", numero_menor)