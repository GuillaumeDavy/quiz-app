# Ce fichier contient toutes les fonctions de base de données 
# permettant de faciliter la connexion à la base, l'éxécution des scripts et la fermeture de la connexion
# Il est inclu dans le fichier db_utils.py et db_reordering.py

import sqlite3

def connectdb():
    path = "../db-quiz.db"
    db_connection = sqlite3.connect(path)
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    # start transaction
    cur.execute("begin")
    return cur, db_connection

def execdb(db):
    #send the request
    db.commit()
    db.rollback()

def closeCursor(cur, db):
    #in case of exception, roolback the transaction
    cur.close()
    db.close()