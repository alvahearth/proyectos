from usuarios import acciones

print("""
    Bienvenid a nuestrp banco
    
    1.- registrarse
    2.- Iniciar sesión
    """)

haz_el = acciones.ACCIONES()
opcion = input("Qué vas a escoger: ")
if opcion == "1":
    haz_el.registrarse()

elif opcion == "2":
    pass