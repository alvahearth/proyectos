print("¿Cúal es el monto del descuento?")
print("--------------------------------------")
precio = input("Ingrese el precio del producto: ")
print("--------------------------------------")

porcentajee = input(
    "Ingrese el porcentaje del descuento(solo numeros de 0 a 99): ")
print("--------------------------------------")

try:
    monto = int(precio)

except:
    print("Monto invalido, ingresa solo números")
    quit()

try:
    porcentaje = float(porcentajee)
    if porcentaje >= 100.0:
        print("Fuera del rango")
        quit()
except:
    print("Monto invalido, ingresa solo números")
    quit()

descuento_total = (monto / 100) * porcentaje
precio_final = monto - descuento_total


print("El monto total del descuento es de:", descuento_total)
print("Y el precio final es de:", precio_final)
