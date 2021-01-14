def tiempo(dia,siguiente_dia):
    
    dias = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    
    for i in dias:
        if dia in i:
            indice = dias.index(dia)
            otro_dia = dias[indice:indice + siguiente_dia + 1]
            el_dia = otro_dia[-1]
            print(el_dia)
            
            
            
            
            while siguiente_dia > int(len(dias)):
                siguiente_dia = dias.index("monday")
                otro_dia = dias[::]
                print(otro_dia)
                
                dia = otro_dia[0]
                break
            
            indice = dias.index(dia)
            otro_dia = dias[indice:indice + siguiente_dia - siguiente_dia + 9]
            el_dia = otro_dia[-1]
            print(el_dia)
            
            
            
            


            # indice = dias.index(dia)
            # if indice + siguiente_dia >= 6:
            #     otro_dia = dias[0]
            #     otro_dia = dias[siguiente_dia + 1]
            #     print(otro_dia)
            # otro_dia = dias[siguiente_dia + 1]
            # print(otro_dia)





tiempo("monday",9)