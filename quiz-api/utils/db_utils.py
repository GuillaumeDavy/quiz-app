import sqlite3
import os

def connect():
    #déclaration des variables
    path = "../../db-quiz.db"

    #création d'un objet connection
    db_connection = sqlite3.connect(path)
    # set the sqlite connection in "manual transaction mode"
    # (by default, all execute calls are performed in their own transactions, not what we want)
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    # start transaction
    cur.execute("begin")
    # TODO methode dinsert de ce quon veut
    # save the question to db
    insertion_result = cur.execute(
        f"insert into Question (title, text, position, image) values"
        f"('{input_question.title}')")

    #send the request
    cur.execute("commit")

    #in case of exception, roolback the transaction
    cur.execute('rollback')
    cur.close()
    db_connection.close()