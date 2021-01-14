print("Bienvenido a la aplicación para convertir de grados celsius y fahrenheit y viceversa")
print("------------------------------------------------------------------------------------")
print("Elige una de las siguientes opciones")
print("celsius")
print("fahrenheit")

user_r = input("Ingresa que sistema de temperatura utilizas: ")
user_t = input("Ingresa la temperatura deseada: ")
user_choice = user_r

try:
    user_temperature = int(user_t)
    if user_temperature < -50 and user_temperature > 200:
        ("out of range")
except:
    print("Cáracter invalido")
    quit()

temperature = ""
if user_choice == "celsius":
    print("La temperatura en grados celsius es: ",user_temperature)
elif user_choice == "fahrenheit":
    print("La temperatura en grados fahrenheit es :",user_temperature)
else:
    print("chao")
    quit()
    
    
temperature = user_choice


if temperature == "celsius":
    temperature = (user_temperature * 1.8) + 32
    print("La temperatura en grados fahrenheit es:",temperature)
elif temperature == "fahrenheit":
    temperature = (user_temperature - 32) / 1.8
    print("La temperatura en grados celsius es:",temperature)

#print("La temperatura final es",temperature)
    