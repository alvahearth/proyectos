from tkinter import *

class Ventana_principal:
    def __init__(self):        
        self.ventana = Tk()
        self.tamaño = "800x600"
        self.width = 300
        self.height = 200
        
    def ventana_padre(self):
        self.ventana.title("Mi primer programa")
        self.ventana.geometry(self.tamaño)
        
        ###########################################################
        self.marco_padre = Frame(self.ventana, width=self.width, height=self.height)
        
        self.marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

        self.cuadro_principal1 = Frame(self.marco_padre, width=self.width, height=self.height)
        color_cuadro_1 = "blue"
        self.cuadro_principal1.config(
            bg=color_cuadro_1,
            bd=5,
            relief="solid"
        )
        self.cuadro_principal1.pack(side=LEFT, anchor=SW)
        self.cuadro_principal1.pack_propagate(False)
        self.añadir_texto(self.cuadro_principal1, color_cuadro_1, "texto")
        
        self.cuadro_principal2 = Frame(self.marco_padre, width=self.width, height=self.height)
        color_cuadro_2 = "red"
        self.cuadro_principal2.config(
            bg=color_cuadro_2,
            bd=5,
            relief="solid"
        )
        self.cuadro_principal2.pack(side=RIGHT, anchor=SE)
        self.cuadro_principal2.pack_propagate(False)
        self.añadir_texto(self.cuadro_principal2, color_cuadro_2, "texto")
        #################################################################
        
        ###############################################################
        self.marco_padre2 = Frame(self.ventana, width=self.width, height=self.height)
        self.marco_padre2.pack(side=TOP, anchor=N, fill=X, expand=YES)
        
        self.cuadro_principal1 = Frame(self.marco_padre2, width=self.width, height=self.height)
        color_cuadro_1 = "crimson"
        self.cuadro_principal1.config(
            bg=color_cuadro_1,
            bd=5,
            relief="solid"
        )
        self.cuadro_principal1.pack(side=LEFT)
        self.cuadro_principal1.pack_propagate(False)
        
        self.añadir_texto(self.cuadro_principal1, color_cuadro_1, "texto")
        
        self.cuadro_principal2 = Frame(self.marco_padre2, width=self.width, height=self.height)
        color_cuadro_2 = "orange"
        self.cuadro_principal2.config(
            bg=color_cuadro_2,
            bd=5,
            relief="solid"
        )
        self.cuadro_principal2.pack(side=RIGHT)
        self.cuadro_principal2.pack_propagate(False)
        
        self.añadir_texto(self.cuadro_principal2, color_cuadro_2, "otro texto")
        ####################################################################
        
    def añadir_texto(self, frame, bg_color, texto):
        text = Label(frame, text=texto)
        text.config(
            fg="white",
            bg=bg_color
        )
        text.pack(fill=Y, expand=YES, anchor=CENTER)
    
    def cuadro3(self):
        cuadro3 = Label(self.cuadro_principal3, text="This is my text")
        cuadro3.config(
            bg="teal"
        )
        cuadro3.pack(side=TOP)
        
    def crear_cuadro_padre(self, frame, bg_color):
        cuadro_padre1 = Frame(frame, width=self.width, height=self.height)
        cuadro_padre1.config(
            bg=bg_color
        )
        self.marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)
        
    
    def refrescar_pantalla(self):
        self.ventana.mainloop()
        
ventana = Ventana_principal()
ventana.ventana_padre()
#ventana.cuadro1()
#ventana.cuadro2()
#ventana.cuadro2()
#ventana.cuadro3()
ventana.refrescar_pantalla()