from mysql import connector

def establecer_conexion():
    database = connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="datos_banco",
        port=3306
    )
    
    cursor = database.cursor(buffered=True)
    
    return [database, cursor]