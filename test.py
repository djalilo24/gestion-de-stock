
import mysql.connector
import traceback

import threading
import time

def test_mysql_connection():
    print("A - Début du thread", flush=True)

    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="YOUR_PASSWORD",
            database="nakhla",
            connection_timeout=5
        )

        print("B - Connexion réussie", flush=True)
        db.close()

    except Exception as e:
        print("C - Erreur :", repr(e), flush=True)

thread = threading.Thread(
    target=test_mysql_connection,
    daemon=True
)
thread.start()

print("D - Thread lancé", flush=True)

