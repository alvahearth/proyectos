
class Calculator:
    
    pay_increase = 1.05
    
    def __init__(self,num_1,num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        
    def suma(self,num_2):
        return self + num_2
    
    def resta(self,num_2):
        return self - num_2
    
    def multi(self,num_2):
        return self * num_2
    
    def

while True:
    
    print("""
        What do you want to do: 
        
        1.- Sum
        2.- Resta
        3.- Multi""")
    
    selection = input("What's your choice: ")
    try:
        sl = int(selection)
        if sl > 3 or sl < 1:
            print("Invalid")
    except:
        print("Invalid choice")
    
    number_1 = input("Enter your first number: ") 
    number_2 = input("Enter your second number: ")

    try:
        x = int(number_1)
        y = int(number_2)
    except:
        print("Those are not numbers")
        
    if sl == 1:
        result = Calculator.suma(x,y)
    if sl == 2:
        result = Calculator.resta(x,y)
    if sl == 3:
        result = Calculator.multi(x,y)
    print(result)