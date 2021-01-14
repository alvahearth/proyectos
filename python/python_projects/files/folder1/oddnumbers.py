user_number = int(input("Ingresa un número: "))
n = int(input("Por qué número lo vas a dividir: "))
resultado = user_number / n
print(resultado)

if user_number % 2 == 0:
    print("Par")
    if user_number % 4 == 0:
        print("Multiplo de 4")
else:
    print("Primo")