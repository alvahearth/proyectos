from usuarios_banco import acciones

print("Bienvenido a banco credichile")
print("""
    Registrate con nosotros hoy día y recibe un bono de 100.000
    
    1.- registrarse
    2.- ingresa a tu cuenta
    """)

opcion = input("Ingresa tu eleccion: ")

realiza_el = acciones.Acciones()
if opcion == "registrarse" or opcion == "1":
    realiza_el.registro()
    
elif opcion == "Ingresar" or opcion == "2":
    realiza_el.login()