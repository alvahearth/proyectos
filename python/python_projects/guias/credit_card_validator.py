def validator(x):
    fixed_list = []
    new_list = []
    c = x.split()
    for char in c:
        for d in char:
            new_list.append(d)
            
    for y_value in new_list[1::2]:
        fixed_list.append(int(y_value))
    
    for x_value in new_list[::2]:
        x_value = int(x_value) * 2
        a = int(x_value)
        if a > 9:
            x = str(x_value)
            c = x.split()
            for a in c:
                a = int(a[0]) + int(a[1])
                fixed_list.append(a)
        else:
            fixed_list.append(a)
    
    result = 0
    for i in fixed_list:
        result = result + i
        
    if result % 10 == 0:
        print("Valid card")
    else:
        print("Invalid card")

if __name__ == "__main__":
    while True:
        print(""" Welcome to the credit card validator
            
            Enter your 16 digit card below 
            """)
    
        user_input = input("Enter the numbers of your card: ")
    
        if len(user_input) > 16:
            print("That's more than sixteen characters")
            continue
        
        validator(user_input)