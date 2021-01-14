from tkinter import *

class IniciarPantalla:
    def __init__(self):
        self.ventana = Tk()
        self.window_size = "600x500"
        self.resize = False
        
    def mostrar_pantalla(self):
        self.ventana.geometry(self.window_size)
        
        if self.resize == False:
            self.ventana.resizable(0, 0)
        else:
            self.ventana.resizable(1,1)
        
    def mostrar_texto(self, contenido):
        texto = Label(self.ventana, text=contenido)
        if contenido is not "hola":
            texto.pack(side=BOTTOM)
        else:
            texto.pack(side=TOP)
        
    def refrescar(self):
        self.ventana.mainloop()


algo = IniciarPantalla()
algo.mostrar_pantalla()

algo.mostrar_texto("hola")
algo.mostrar_texto("chao")

algo.refrescar()