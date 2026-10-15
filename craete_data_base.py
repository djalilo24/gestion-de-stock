
import mysql.connector
from mysql.connector import Error

db = None
sql = None

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="guelma24@"
    )

    print("Connexion MySQL réussie")

    sql = db.cursor()

    sql.execute("""
        CREATE DATABASE IF NOT EXISTS NAKHLA
        CHARACTER SET utf8mb4
        COLLATE utf8mb4_unicode_ci
    """)

    print("Base de données NAKHLA créée avec succès")

except Error as e:
    print("Erreur MySQL :", e)

finally:
    if sql is not None:
        sql.close()

    if db is not None and db.is_connected():
        db.close()
        print("Connexion MySQL fermée")
