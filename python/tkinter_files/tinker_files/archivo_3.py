from tkinter import *

ventana = Tk()



cuadro_algo = Label(ventana, text="This is my program")
cuadro_algo.config(
    bg="black",
    fg="white"
)
cuadro_algo.pack(side=TOP, fill=X, expand=YES)

cuadro_principal = Frame(ventana, width=200, height=200)
cuadro_principal.pack(side=TOP, fill=X, expand=YES)

cuadro_1 = Label(cuadro_principal, text="Primer texto")
cuadro_1.config(
    bg="red"
)
cuadro_1.pack(side=RIGHT,anchor=NE)

cuadro_2 = Label(cuadro_principal, text="Segundo texto")
cuadro_2.config(
    bg="blue"
)
cuadro_2.pack(side=LEFT ,anchor=NW)

ventana.mainloop()