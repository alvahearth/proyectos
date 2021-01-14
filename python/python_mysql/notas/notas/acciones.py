from notas import modelo_notas

class Acciones:
    
    def crear_nota(self, usuario):
        self.usuario_id = usuario[0]
        self.titulo = input("Crear nota: ")
        self.contenido = input("Ingresa el contenido de tu nota: ")
        
        nueva_nota = modelo_notas.Nota(self.usuario_id, self.titulo, self.contenido)
        nota_x = nueva_nota.nueva_nota()
        
        if nota_x[0] >= 1:
            print("La nota se ha creado exitosamente")
            
    def mostrar_nota(self, usuario):
        self.usuario_id = usuario[0]
        
        nota_para_mostrar = modelo_notas.Nota(self.usuario_id,"","")
        nota_x = nota_para_mostrar.mostrar()
        
        print(nota_x)
        
    def eliminar_nota(self, usuario):
        self.usuario_id = usuario[0]
        self.titulo = input("Indica el titulo de la nota a borrar: ")
        
        nota_para_borrar = modelo_notas.Nota(self.usuario_id, self.titulo, "")
        nota_x = nota_para_borrar.borrar()
        
        
        
        