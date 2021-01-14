usp = input("Ingresa el monto: ")

try:
    dolar = float(usp)
except:
    quit()

tasadecambio = dolar * 810

print(tasadecambio)
