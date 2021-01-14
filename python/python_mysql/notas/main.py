from usuarios import acciones

print("""
    Bienvenido al sistema de productos
    
    1.- registro
    2.- login
    """)

opcion = input("Ingresa tu opcion: ")

haz_el = acciones.Acciones()
if opcion == "registro" or opcion == "1":
    haz_el.registro()

if opcion == "login" or opcion == "2":
    haz_el.identificacion()