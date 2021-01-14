def power(x,y):
    multiplicador = 0
    potencia = 0
    while potencia < y:
        potencia = x ** multiplicador
        multiplicador = multiplicador + 1
        print(potencia)       
        

if __name__ == "__main__":
    numero =int(input("Escibre un número: "))
    limite = int(input("Hasta qué número quieres ver: "))
    power(numero,limite)