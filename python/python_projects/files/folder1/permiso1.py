def numeros(x):
    if x == 5:
        return "el numero es 5"
    elif x == 10:
        return "el numero es 10"
    else:
        return "el numero es muy grande"

print(numeros(20))
print("Pero sigue intentando")
print(numeros(10))
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
try:
     permiso = int(edad)
except:
    print("Ingresa numeros porfavor")
    quit()

edadFinal = int(edad)
if edadFinal <= 18:
    print("No tienes permiso para salir")
else:
    print("Puedes hacer lo que quieras") 