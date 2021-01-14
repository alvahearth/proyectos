def disemvowel(string):
    
    #Stores the vowels to make comparisons later
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    
    #The string will be stored in this list
    word = []
    
    #This will be a list with no vowels
    no_vowels = []
    
    #This will be the string in wich we will store the new string
    new_string = ""
    
    #Here we will create the list with all the letters
    for i in string:
        word.append(i)
    
    #And here we will check if there are vowel in the word[list] and exclude them
    for i in word:
        if i in vowels:
            continue
        else:
            no_vowels.append(i)
    
    #And finally we will create the new string combining all the remaining consonants
    for i in no_vowels:
        new_string = new_string +  i
    
    return new_string


disemvowel("This website is for losers LOL!")

