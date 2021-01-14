from logging import setLoggerClass
from usuarios_banco import conexion
import hashlib

connect = conexion.establecer_conexion()
database = connect[0]
cursor = connect[1]

class Usuario:
    def __init__(self, nombre, apellido, clave, dinero):
        self.nombre = nombre
        self.apellido = apellido
        self.clave = clave
        self.dinero = dinero
        
    def crear_usuario(self):
        clave_encriptada = hashlib.sha256()
        clave_encriptada.update(self.clave.encode("utf8")) 
        
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s )"
        info = (self.nombre, self.apellido, clave_encriptada.hexdigest(), self.dinero)
        
        cursor.execute(sql, info)
        database.commit()
        
        return [cursor.rowcount, self] 
    
    def identificarse(self):
        clave_encriptada = hashlib.sha256()
        clave_encriptada.update(self.clave.encode("utf8"))
        
        sql = "SELECT * FROM usuarios WHERE nombre = %s AND clave = %s"
        info = (self.nombre, clave_encriptada.hexdigest())
        
        cursor.execute(sql, info)
        
        result = cursor.fetchone()
        
        return result
    
    def ver_balance():
        sql = "SELECT * FROM usuarios LIMIT 4,1"
        
        cursor.execute(sql)
        database.commit()
        
        result = cursor.fetchone()
        
        return result
    
    def retirar_balance(self):
        sql = f"UPDATE usuarios SET dinero = {self.dinero} WHERE nombre LIKE '%{self.nombre}%' "
        
        cursor.execute(sql)
        database.commit()
    
        return cursor.rowcount
    
    def abonar_balance(self):
        sql = f"UPDATE usuarios SET dinero = {self.dinero} WHERE nombre LIKE '%{self.nombre}%' "
        
        cursor.execute(sql)
        database.commit()
        
        return cursor.rowcount