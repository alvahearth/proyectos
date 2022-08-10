def validar_rut(value):
    print(value)

    numeroi = str(value)

    lista_numeros = []

    verificador = int(numeroi[8])

    contador = 2
    for i in numeroi[7::-1]:
        if contador > 7:
            contador = 2
        numero = contador * int(i)
        contador += 1
        lista_numeros.append(numero)

    sumatoria = 0
    for j in lista_numeros:
        sumatoria += j

    division = int(sumatoria / 11)
    multiplicado = division * 11
    final = 11 - (sumatoria - multiplicado)

    if final != verificador:
        return 1
    else:
        return 2

user_i = int(input('Ingresa tu rut: '))

chekc = validar_rut(user_i)

if chekc == 1:
    print('rut invalido')

elif chekc == 2:
    print('rut válido')



