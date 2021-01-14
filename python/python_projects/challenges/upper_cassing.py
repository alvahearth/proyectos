def to_jaden_case(string):
    
    #We initialized an empty list to store our future list of words split into sentences
    lista = []
    
    #And also a empty string to store our new string
    new_string = ""
    
    #We split up the string into sentences with the split method
    x = string.split()
    
    #We capitalize each sentence and we append them to the list with a blank space
    for i in x:
        e = (i.capitalize())
        lista.append(e+" ")

    #And now we loop the list we just created and create our new string properly capitalized
    for i in lista:
        new_string = new_string + i  
        
    #And finally we remove the whitespace at the end
    return new_string.strip()

quote = to_jaden_case("How can mirrors be real if our eyes aren't real")

print(quote)