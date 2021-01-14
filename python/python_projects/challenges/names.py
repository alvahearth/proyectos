def friend(x):
    new_friends = []
    for i in x:
        if len(i) == 4:
            new_friends.append(i)
            
    return new_friends  
            
    
    
x = friend((["Ryan", "Kieran", "Mark",]))
print(x)