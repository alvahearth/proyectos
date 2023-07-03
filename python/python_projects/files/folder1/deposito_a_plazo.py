def deposito(monto,fondo,meses):
    ganancias = 0
    if fondo == 1:
        for i in range(1,meses+1):
            ganancias = monto * 0.12
            return ganancias + monto
    elif fondo == 2:
        for i in range(1,meses+1):
            ganancias = monto * 0.13
            return ganancias + monto
    elif fondo == 3:
        for i in range(1,meses+1):
            ganancias = monto * 0.14
            return ganancias + monto
    elif fondo == 4:
        for i in range(1,meses+1):
            ganancias = monto * 0.15
            return ganancias + monto


while True:
    print("""
        Bienvenido al calculador de ganancia en formato de déposito a plazo
        
        """)

    plata = int(input("Cuanto dinero piensas invertir: "))

    print(""" 
        Elige uno de los fondos disponibles
        
        a.- Fondo A : 0,12%
        c.- Fondo B : 0,13%
        b.- Fondo C : 0,14%
        d.- Fondo D : 0,15%
        
        """)
    fondo = input("Cuál es tu elección: ")
    if fondo is "a" or fondo is "b" or fondo is "c" or fondo is "d":
        print(f"Has seleccionado la opción {fondo}")
        if fondo == "a":
            fondo = 1
        elif fondo == "b":
            fondo = 2
        elif fondo == "c":
            fondo = 3
        elif fondo == "d":
            fondo = 4
    else:
        print("Opción invalida")
        continue
        
    meses = input("Por cuantos meses tienes pensado renovar: ")
    try:
        number = int(meses)
        if number > 48:
            print("Solo puedes hacer una observación hasta 2 años (48 meses)")
            number = 48
            print("Hemos cambiado tu solicitud a 48 meses")
            x = input("Estas de acuerdo con esta decisión (si/no): ")
            if x == "si":
                print("Entendidom seguiremos con la operación")
            elif x == "no":
                print("Entendido, te preguntaremos de nuevo")
                continue
            
    except:
        print("Esa no es una opción valida")
        continue
    
    resultado = deposito(plata,fondo,number)
    print(resultado)
