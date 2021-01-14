import sys

from mysql.connector.errors import ProgrammingError
from usuarios_banco import modelo_usuario

class Acciones:
    
    def registro(self):
        print("Genial, vamos a registrarnos")
        self.nombre = input("Ingresa tu nombre: ")
        self.apellido = input("Ingresa tu apellido: ")
        self.clave = input("Registra tu clave (Debe tener 4 digitos): ")
        if len(self.clave) != 4:
            print("Tu clave debe tener exacto 4 digitos")
            sys.exit()
        
        self.dinero = 100000
        
        nuevo_usuario = modelo_usuario.Usuario(self.nombre, self.apellido, self.clave, self.dinero)
        usuario_x = nuevo_usuario.crear_usuario()
        
        if usuario_x[0] >= 1:
            print(f"Felicitaciones {usuario_x[1].nombre} Tu cuenta se ha creado exitosamente y conseguiste {self.dinero} como regalo")
        else:
            print("Lo sentimos pero no te has podido registrar")
            
    def login(self):
        print("Ingresa tu credenciales")
        self.nombre = input("Ingresa tu nombre: ")
        self.clave = input("Ingresa tu clave: ")
        
        usuario_registrado = modelo_usuario.Usuario(self.nombre,"",self.clave, "")
        usuario_x = usuario_registrado.identificarse()
        
        if usuario_x[0] >= 1:
            print(f"Bienvenido {self.nombre} a tu banco")
            self.sistema_interno(usuario_x)
        else:
            print("No estás registrado, te recomendamos que te registres primero")
            
            
    #Sistema de dinero
    def mostrar(self, dinero_usuario):
        self.balance = dinero_usuario[4]
        print(f"Este es tu balance: {self.balance}")
        
    def retirar_dinero(self, dinero_restante):
        self.dinero = input("Cuando dinero vas a retirar: ")
        try:
            plata = int(self.dinero)
        except:
            print("Tiene que ser un valor númerico")
            sys.exit()
            
        result = dinero_restante[4] - plata
        
        dinero_a_retirar = modelo_usuario.Usuario(dinero_restante[1],"","", result)
        dinero_x = dinero_a_retirar.retirar_balance()
        print(dinero_x)
        
        if dinero_restante[4] <= 0 or (dinero_restante[4] - plata <= 0):
            print("Hubo un error y no pudimos operar correctamente tu transacción")
        else:
            print(f"Retiraste {plata} exitosamente ")
        
    def abonar_dinero(self, usuario):
        self.dinero = input("Cuanto dinero vas a abonar a tu cuenta: ")
        try:
            plata = int(self.dinero)
        except:
            print("Ingresa solo valores numericos")
            sys.exit()
            
        result = usuario[4] + plata
        
        dinero_a_abonar = modelo_usuario.Usuario(self.nombre, "", "", result)
        dinero_x = dinero_a_abonar.abonar_balance()
        
        if usuario[0] >= 1:
            print(f"Abonaste {self.dinero} exitosamente a tu cuenta")
        else:
            print("Hubo un error, intenta nuevamente")
            
            
    def sistema_interno(self, usuario):
        print("""Bienvenido a tu banca personal
            
            1.- Ver balance
            2.- Retirar dinero
            3.- Abonar dinero"""
        )
        
        opcion = input("Qué vas a hacer: ")
        
        if opcion == "1":
            self.mostrar(usuario)
            self.sistema_interno(usuario)
            
        elif opcion == "2":
            self.retirar_dinero(usuario)
            self.sistema_interno(usuario)
    
        elif opcion == "3":
            self.abonar_dinero(usuario)
            self.sistema_interno(usuario)
    