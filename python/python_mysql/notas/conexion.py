from mysql import connector

def establecer_conexion():
    database = connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="base_prueba",
        port=3306
    )
    
    cursor = database.cursor()
    
    return [database, cursor]