from os import curdir

from mysql.connector import cursor
import hashlib
from usuarios import conexion

connect = conexion.establecer_conexion()
database = connect[0]
cursor = connect[1]

class Usuario:
    def __init__(self, nombre, apellido, rut, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.contraseña = contraseña
        
    def crear_usuario(self):
        encriptado = hashlib.sha256()
        encriptado.update(self.contraseña.encode("utf8"))
        
        sql = "INSERT INTO usuario VALUES(null, %s, %s, %s, %s)"
        info = (self.nombre, self.apellido, self.rut, encriptado.hexdigest())
        
        cursor.execute(sql, info)
        database.commit()
        
        return [cursor.rowcount, self]
        
    def verificar_usuario(self):
        encriptado = hashlib.sha256()
        encriptado.update(self.contraseña.encode("utf8"))

        sql = "SELECT * FROM usuario WHERE rut = %s AND contraseña = %s"
        info = (self.rut, encriptado.hexdigest())

        cursor.execute(sql, info)

        result = cursor.fetchone()

        return result