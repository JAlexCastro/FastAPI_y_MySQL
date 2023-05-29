#Package MySQL
import mysql.connector
from mysql.connector import Error

#Package Decouple
from decouple import config


#Conexion
try:
    conexion = mysql.connector.connect(
        host = config("host"),
        port = config("port"),
        user = config("user"),
        password = config("password"),
        db = "storedb"
    )

except Error as e:
    print(f"Conexion error: {e}")

#Cursor
cursor = conexion.cursor()


#Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS tbl_users(User_id INTEGER PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(100) NOT NULL,Last_name VARCHAR(100) NOT NULL, Email VARCHAR(100) NOT NULL UNIQUE, Password VARCHAR(250) NOT NULL)")
conexion.commit()


