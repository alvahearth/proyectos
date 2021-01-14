print("****************************************************")
print("*Bienvenido al sistema de cálculo de subscripciones*")
print("****************************************************")
print("Ingresa una de las siguientes opciones")
print("1.- Netflix")
print("2.- Spotify")
print("3.- Gamepass")
print("")

nombreServicio = input("Ingrese el numero del servicio: ")

if nombreServicio == "1":
    tipoDePago = input("Cuantos meses vas a pagar: ")
    try:
        mes = int(tipoDePago)
        if mes < 1 or mes > 12:
            print("fuera de rango")
            quit()
    except:
        print("Solo números")
        quit()

    if mes > 0 or mes < 13:
        calculoFinal = input("Ingresa el monto que pagas al mes: ")
        try:
            dinero = int(calculoFinal)
            montoaPagar = dinero * mes
            print("El monto que vas a pagar en Netflix es:", montoaPagar)
        except:
            print("invalido")
            quit()

elif nombreServicio == "2":
    tipoDePago = input("Cuantos meses vas a pagar: ")
    try:
        mes = int(tipoDePago)
        if mes < 1 or mes > 12:
            print("fuera de rango")
            quit()
    except:
        print("Solo números")
        quit()

    if mes > 0 or mes < 13:
        calculoFinal = input("Ingresa el monto que pagas al mes: ")
        try:
            dinero = int(calculoFinal)
            montoaPagar = dinero * mes
            print("El monto que vas a pagar de Spotify es:", montoaPagar)
        except:
            print("invalido")
            quit()

elif nombreServicio == "3":
    tipoDePago = input("Cuantos meses vas a pagar: ")
    try:
        mes = int(tipoDePago)
        if mes < 1 or mes > 12:
            print("fuera de rango")
            quit()
    except:
        print("Solo números")

        quit()

    if mes > 0 or mes < 13:
        calculoFinal = input("Ingresa el monto que pagas al mes: ")
        try:
            dinero = int(calculoFinal)
            montoaPagar = dinero * mes
            print("El monto que vas a pagar de Gamepass es:", montoaPagar)
        except:
            print("invalido")
            quit()

else:
    print("Ingresa uno de los números en pantalla")
    quit()
