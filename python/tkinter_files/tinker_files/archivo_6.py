from tkinter import *

ventana = Tk()
ventana.geometry("400x400")

def get_texto1():
    resultado_1.set(texto.get())
    
def get_num1():
    resultado_2.set(num1.get())
    
texto = StringVar()
resultado_1 = StringVar()

num1 = IntVar()
resultado_2 = IntVar()

Label(ventana, text="Mucho texto").pack(side=TOP, anchor=N)
Entry(ventana, textvariable=texto).pack(side=TOP, anchor=N)

Label(ventana, textvariable=resultado_1).pack(side=TOP, anchor=N)

Button(ventana, command=get_texto1, text="Push me").pack(side=TOP, anchor=N)

Label(ventana, text="Mucho numero").pack(side=TOP, anchor=N)
Entry(ventana, textvariable=num1).pack(side=TOP, anchor=N)

Label(ventana, textvariable=resultado_2).pack(side=TOP, anchor=N)

Button(ventana, command=get_num1, text="Push me").pack(side=TOP, anchor=N)

ventana.mainloop()