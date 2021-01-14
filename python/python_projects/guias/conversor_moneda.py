def conversor(x,y):
    if x == 1:
        r = y * 0.00127
        r = round(r,2)
        return r
    elif x == 2:
        r = y * 0.0136
        r = round(r,2)
        return r
    elif x == 3:
        r =  y * 0.000266
        r = round(r,2)
        return r
    elif x == 4:
        r = y * 0.04514
        r = round(r,2)
        return r

if __name__ == '__main__':
    while True:
        print("-----------------------------------------------")
        print("Bienvenido al programa de conversor de monedas")
        print("1.- Pesos chilenos a dolar")
        print("2.- Pesos argentinos a dolar")
        print("3.- Pesos colombianos a dolar")
        print("4.- Pesos mexicanos a dolar")
        print("")
        tipo_de_moneda = input("Ingresa tu elección: ")
        if tipo_de_moneda == "done":
            break
        try:
            tipo = int(tipo_de_moneda)
            
        except:
            print("invalid")
            continue
        global dinero
        dinero = input("Ingresa la cantidad de dinero:")
        try:
            cantidad = int(dinero)
        except:
            print("Invalido")
            continue        

        resultado = conversor(tipo,cantidad)
        
        print("Tienes " , resultado , " en dolares")
    