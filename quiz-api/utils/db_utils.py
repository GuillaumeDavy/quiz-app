from email.mime import image
import sqlite3
import os
from turtle import position

def connectdb():
    path = "../db-quiz.db"
    db_connection = sqlite3.connect(path)
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    # start transaction
    cur.execute("begin")
    return cur, db_connection

def execdb(db, cur):
    #send the request
    db.commit()

    #in case of exception, roolback the transaction
    db.rollback()
    cur.close()
    db.close()

def deleteQuestion(position):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Requete de suppression de question en base de données
    print("delete from question where position = " + position)
    deletion_result = cur.execute(
        f"delete from question where position = '{position}'")

    #Exécution de la requete
    execdb(db_connection, cur)


def insertQuestion(input_question):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Formatage des valeurs
    title = input_question.title.replace("'", "\'")
    text = input_question.text.replace("'", "\'")
    position = input_question.position
    image = input_question.image.replace("'", "\'")

    #Requete d'insertion de question en base de données
    insertion_result = cur.execute(
        f"insert into question (position, text, title, image) values"
        f'("{position}", "{text}", "{title}", "{image}")')

    #Exécution de la requete
    execdb(db_connection, cur)

def insertAnswer(answerObject):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Formatage des valeurs
    is_correct = answerObject.is_correct
    text = answerObject.text.replace("'", "\'")
    question_position = answerObject.question

    #Requete d'insertion de question en base de données
    insertion_result = cur.execute(
        f"insert into answer (is_correct, text, question_position) values"
        f'("{is_correct}", "{text}", "{question_position}")')

    #Exécution de la requete
    execdb(db_connection, cur)