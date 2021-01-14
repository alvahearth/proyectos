from usuarios import modelo_usuario
from notas import acciones as acciones_nota

class Acciones:
    
    def registro(self):
        self.nombre = input("Registra tu nombre: ")
        self.apellido = input("Registra tu apellido: ")
        self.email = input("Registra tu correo: ")
        self.contraseña = input("Registra tu contraseña: ")
        
        nuevo_usuario = modelo_usuario.Usuario(self.nombre, self.apellido, self.email, self.contraseña)
        usuario_x = nuevo_usuario.registrar_usuario()
        
        if usuario_x[0] >= 1:
            print("Usuario registrado correctamente")
            
    def identificacion(self):
        self.email = input("Ingresa el correo que tienes registrado: ")
        self.contraseña = input("Ingresa tu contraseña: ")
        
        usario_en_base = modelo_usuario.Usuario("","",self.email, self.contraseña)
        usuario_x = usario_en_base.identificar_usuario()
        
        if usuario_x[0] >= 1:
            print(f"Eres el usuario {usuario_x[1]}")
            self.siguientes_acciones(usuario_x)
            
    def siguientes_acciones(self, usuario):
        print(f"Bienvenido {usuario[1]} estas son las opciones disponibles" )
        print("""
            1.- Crear nota
            2.- Mostrar nota
            3.- Borrar nota
            4.- Salir
            """)
        
        opcion = input("¿Que deseas hacer?: ")
        
        haz_el = acciones_nota.Acciones()
        if opcion == "crear" or opcion == "1":
            haz_el.crear_nota(usuario)
            self.siguientes_acciones(usuario)
            
        elif opcion == "mostrar" or opcion == "2":
            haz_el.mostrar_nota(usuario)
            self.siguientes_acciones(usuario)
            
        elif opcion == "eliminar" or opcion == "3":
            haz_el.eliminar_nota(usuario)
            self.siguientes_acciones(usuario)