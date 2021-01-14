import conexion

conexion_con_base = conexion.establecer_conexion()
database = conexion_con_base[0]
cursor = conexion_con_base[1]

class Nota:
    def __init__(self, usuario_id, titulo, contenido):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.contenido = contenido
        
    def nueva_nota(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        info = (self.usuario_id, self.titulo, self.contenido)
        
        cursor.execute(sql, info)
        database.commit()
        
        return [cursor.rowcount, self]
    
    def mostrar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        
        cursor.execute(sql)

        result = cursor.fetchall()
        
        return result
    
    def borrar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%' "
        
        cursor.execute(sql)
        database.commit()
        
        return [cursor.rowcount, self]