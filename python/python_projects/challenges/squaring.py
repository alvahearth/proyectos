def square_digits(num):
    
    #We transform the parameter num to a string so we can use the len function
    string = str(num)
    
    #We initialize an empty string so we can store our result
    new_string = ""
    
    #now we loop trough the numbers in the string that we transformed earlier
    for i in string:
        
        ##We procede to square every value as an integer 
        power = int(i) ** 2
        
        #Then we concatenate each value as a string
        new_string += str(power)
        
    print(new_string)
    #And now we return the new value as an integer
    return int(new_string)

square_digits(911926289)