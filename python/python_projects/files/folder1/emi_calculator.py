from matplotlib import pyplot as pit

banks = "Santander","Falabella","Scotiabank","Banco de Chile","otros"

score = [20,20,10,10,40]

explode = (0.1,0,0,0,0)

fig1, ax1 = pit.subplots()

ax1.pie(score,explode=explode,labels=banks,autopct="%1.1f%%",shadow=True,startangle=90)

ax1.axis("equal")

pit.show()
