from tkinter import *

class VentanaPrincipal:
    def __init__(self):
        self.tamaño = "800x600"
        self.width = 300
        self.height = 200
        
    def iniciar(self):
        self.ventana = Tk()
        self.ventana.geometry(self.tamaño)
        
    def crear_cuadros(self, num):
        if num == 1:
            cuadro_padre = self.crear_cuadro_padre(self.ventana, "blue", BOTTOM)
            self.crear_cuadro_hijo(cuadro_padre, "red", RIGHT)
            self.crear_cuadro_hijo(cuadro_padre, "teal", LEFT)
        if num == 2:
            cuadro_padre = self.crear_cuadro_padre(self.ventana, "orange", TOP)
            self.crear_cuadro_hijo(cuadro_padre, "red", RIGHT)
            self.crear_cuadro_hijo(cuadro_padre, "teal", LEFT)
            
    def crear_cuadro_padre(self, frame, bg_color, posicion):
        self.cuadro_padre1 = Frame(frame, width=self.width, height=self.height)
        self.cuadro_padre1.config(
            bg=bg_color
        )
        
        if posicion == BOTTOM:
            self.cuadro_padre1.pack(side=posicion, anchor=S, fill=X, expand=YES)
        elif posicion == TOP:
            self.cuadro_padre1.pack(side=posicion, anchor=N, fill=X, expand=YES)
            
        result = self.cuadro_padre1
        return result
        
    def crear_cuadro_hijo(self ,frame ,bg_color, posicion):
        self.cuadro_hijo = Frame(frame, width=self.width, height=self.height)
        self.cuadro_hijo.config(
            bg=bg_color
        )
        self.cuadro_hijo.pack(side=posicion)
        self.cuadro_hijo.pack_propagate(False)
        self.añadir_texto(self.cuadro_hijo, "texto", bg_color)
        
    def añadir_texto(self, frame, texto, bg_color):
        self.text = Label(frame, text=texto)
        self.text.config(
            bg=bg_color
        )
        self.text.pack(fill=Y, expand=YES, anchor=CENTER)
            
    def refrescar(self):
        self.ventana.mainloop()
        
ventana = VentanaPrincipal()
ventana.iniciar()
ventana.crear_cuadros(1)
ventana.crear_cuadros(2)
ventana.refrescar()