
import mysql.connector
import traceback

print("1 - Début du test", flush=True)

try:
    db = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="guelma24@",
        database="nakhla",
        connection_timeout=5
    )

    print("2 - Connexion réussie", flush=True)
    print("3 - État :", db.is_connected(), flush=True)

    db.close()
    print("4 - Connexion fermée", flush=True)

except BaseException:
    traceback.print_exc()
