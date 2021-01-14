from tkinter import *


#user_input = str(input("Que color te gusta: "))
user_input = int(input("Hasta que número quieres contar: "))

root = Tk()

def myclick():
    lines = 20
    while lines > 0:
        mylabel1 = Label(root,text="holi")
        mylabel1.pack()
        lines = lines - 1
        
def mynumbercount():
    lista = list()
    n = range(1,user_input)
    for i in n:
        lista.append(i)
        mylabel2 = Label(root,text=lista)
        mylabel2.pack()

mybutton = Button(root,text="Click me",padx=20,pady=40,command=myclick)
mybutton1 = Button(root,text="Click me",padx=20,pady=40,command=mynumbercount)

mybutton.pack()
mybutton1.pack()
    
root.mainloop()