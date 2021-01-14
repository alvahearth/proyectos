def arithmetic_arranger(problems,param):
    val1 = problems[0]
    num1_1 = int(val1[0:2])
    num2_1 = int(val1[5:9])
    
    val2 = problems[1]
    num1_2 = int(val2[0:4])
    num2_2 = int(val2[7:10])
    
    val3 = problems[2]
    num1_3 = int(val3[0:3])
    num2_3 = int(val3[5:9])
    
    val4 = problems[3]
    num1_4 = int(val4[0:3])
    num2_4 = int(val4[5:9])
    
    
    y =print("  ", num1_1,"    ", num1_2,"   ",num1_3,"   ",num1_4)
    c =print("+", num2_1,"       ",num2_2,"   ",num2_3,"    ",num2_4)
    b =print("------","   -----","   ----"," -----")
    if param is True:
        print(" ",num1_1 + num2_1,"    ",num1_2 + num2_2,"   ",num1_3 + num2_3,"   ",num1_4 + num2_4)
    return y,c,b






arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)
