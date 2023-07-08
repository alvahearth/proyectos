from matplotlib import pyplot as pit
import math

banks = "Santander","Falabella","Scotiabank","Banco de Chile","otros"

score = [20,20,10,10,40]

explode = (0.1,0,0,0,0)


pit.pie(score,explode=explode,labels=banks,autopct="%1.1f%%",shadow=True,startangle=90)

pit.axis("equal")

pit.show()
