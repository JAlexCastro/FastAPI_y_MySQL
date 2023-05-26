import mysql.connector
from decouple import config
from mysql.connector import Error

conector = mysql.connector.connect(
    host = config("host"),
    port = config("port"),
    user = config("user"),
    password = config("password")
)