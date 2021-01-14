import conexion
import hashlib

conexion_con_base = conexion.establecer_conexion()
database = conexion_con_base[0]
cursor = conexion_con_base[1]


class Usuario:
    def __init__(self, nombre, apellido, email,contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        
    def registrar_usuario(self):
        clave_encriptada = hashlib.sha256()
        clave_encriptada.update(self.contraseña.encode("utf8"))
        
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s)"
        info = (self.nombre, self.apellido, self.email, clave_encriptada.hexdigest())
        
        cursor.execute(sql, info)
        database.commit()
        
        return [cursor.rowcount, self]
    
    def identificar_usuario(self):
        clave_encriptada = hashlib.sha256()
        clave_encriptada.update(self.contraseña.encode("utf8"))
        
        sql = "SELECT * FROM usuarios WHERE email = %s AND contraseña = %s"
        info = (self.email, clave_encriptada.hexdigest())
        
        cursor.execute(sql, info)
        
        result = cursor.fetchone()
        return result