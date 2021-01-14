import math

def conversion(x):
    if x == 1:
        result = (temp * 1.8) + 32
        print("La temperatura en Farenheit es:",result)
    elif x == 2:
        result = float((temp - 32 ) / 1.8)
        result = round(result,2)
        print("La temperatura en Celsius es:",result)
        
if __name__ == "__main__":
    global temp
    print("1.- Celsius")
    print("2.- Farenheit")
    x = input("¿Qué sistema de temperatura utilizas?: ")
    try:
        num = int(x)
        
        #if num < 1 or num > 2:
            #print("out of range")
    except:
        quit()
    temp = float(input("Ingresa la temperatura que quieras: "))
    
    b = conversion(num)
        
    