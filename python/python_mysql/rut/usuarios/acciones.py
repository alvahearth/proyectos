import sys
from usuarios import modelo_usuario

class ACCIONES:
    
    def registrarse(self):
        self.nombre = input("Registra tu nombre: ")
        self.apellido = input("Registra tu apellido: ")
        self.rut = input("Ingresa tu rut: ")
        self.contraseña = input("Registra tu contraseña: ")
    
        if self.verificar_rut(self.rut) is not True:
                print("Rut invalido")
                sys.exit()

        nuevo_usuario = modelo_usuario.Usuario(self.nombre, self.apellido, self.rut, self.contraseña)
        usuario_x = nuevo_usuario.crear_usuario()
            
        if usuario_x[0] >= 1:
            print(f"{usuario_x[1].nombre} tu cuenta ha sido creada exitosamente")
        else:
            print("Hubo un error intenta nuevamente")
        

    def identificarse(self):
        self.rut = input("Ingresa tu rut: ")
        self.contraseña = input("Ingresa tu contraseña: ")

        usuario_registrado = modelo_usuario.Usuario("","",self.rut, self.contraseña)
        usuario_x = usuario_registrado.verificar_usuario()

        if usuario_x[0] >= 1:
            print(f"El usuario {usuario_x[1]} se ha registrado correctamente")
        else:
            print("Error")

        
    def verificar_rut(self, rut):
        self.lista_numeros = []
        self.lista_modificada = []

        for i in rut:
            self.lista_numeros.append(i)

        multiplicador = 2
        for i in self.lista_numeros[7::-1]:
            result = int(i) * multiplicador
            multiplicador = multiplicador + 1
            if multiplicador > 7:
                multiplicador = 2
            self.lista_modificada.append(result)
            
        sumatoria = 0
        for i in self.lista_modificada:
            sumatoria = sumatoria + int(i)
            
        numero_dividido = int(sumatoria / 11)
        otro_numero = numero_dividido * 11
        resta_de_numeros = sumatoria - otro_numero
        final = 11 - resta_de_numeros
        numero_verificador = self.lista_numeros[-1]
        
        if final == int(numero_verificador):
            return True
        else:
            return False