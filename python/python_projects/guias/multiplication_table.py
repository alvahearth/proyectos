def tabla(x,y):
    for i in range(1,y+1):
        print(str(x)+" multiplicado por "+str(i)+" es |",x*i)

if __name__ == "__main__":
    while True:
        print(""" Estás son las tablas de multiplicar

        ¿Qué tabla quieres ver?

        1.-  Tabla del 1
        2.-  Tabla del 2
        3.-  Tabla del 3
        4.-  Tabla del 4
        5.-  Tabla del 5
        6.-  Tabla del 6
        7.-  Tabla del 7
        8.-  Tabla del 8
        9.-  Tabla del 9
        10.- Tabla del 10
        esc.- Salir
        """)

        option = input("Qué tabla quieres ver: ")
        if option == "esc":
            break
        try:
            number = int(option)
        except:
            print("Esa no es una opción")
            quit()
        multi = input("Hasta que número quieres ver la tabla: ")
        try:
            multiplo = int(multi)
        except:
            print("No es un número")
            quit()
        
        if number == 1:
            tabla(number,multiplo)
        elif number == 2:
            tabla(number,multiplo)
        elif number == 3:
            tabla(number,multiplo)
        elif number == 4:
            tabla(number,multiplo)
        elif number == 5:
            tabla(number,multiplo)
        elif number == 6:
            tabla(number,multiplo)
        elif number == 7:
            tabla(number,multiplo)
        elif number == 8:
            tabla(number,multiplo)
        elif number == 9:
            tabla(number,multiplo)
        elif number == 10:
            tabla(number,multiplo)