






if __name__ == "__main__":
    intentos = 3
    while True:
        key = input("Ingresa tu clave: ")
        if intentos <= 1:
            print("Clave bloqueada")
            quit()
        if key == "hola":
            print("Welcome")
            break
        else:
            print("Invalid key")
            intentos = intentos - 1
            print("Te quedan " + str(intentos))
            continue

    money = 20000
    
    while True:
        print(""" Banking app

        ¿What will you do?
        
        1.- "Withdraw money"
        2.- "See balance"
        3.- "Exit"
        """)
        user = input("Select your option: ")
        if user == "1":
            money_w = input("How much money will you withdraw: ")
            try:
                w = int(money_w)
            except:
                print("Invalid operation")
                continue
            print("You withdrew "+str(w))
            money = money - w
            if money < 0:
                print("Not enough funds")
                continue
            print("")
            print("You have "+str(money)+" left")
            
        elif user == "2":
            print("You have "+str(money)+" left")
        elif user == "3" or "exit":
            print("Have a nice day")
            break
        else:
            print("Invalid operation: ")
            continue