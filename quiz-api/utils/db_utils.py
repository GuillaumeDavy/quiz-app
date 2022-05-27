from email.mime import image
import sqlite3
import os
from turtle import position

from app import PutQuestion

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

def deleteQuestion(position):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Requete de suppression de question en base de données
    deletion_result = cur.execute(
        f"delete from question where position = '{position}'")

    #Exécution de la requete
    execdb(db_connection)

    closeCursor(cur, db_connection)

def deleteAnswer(position):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Requete de suppression de question en base de données
    deletion_result = cur.execute(
        f"delete from answer where question_position = '{position}'")

    #Exécution de la requete
    execdb(db_connection)

    closeCursor(cur, db_connection)


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
    execdb(db_connection)

    closeCursor(cur, db_connection)

def getQuestion(position):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Requete de récupération des questions en base de données
    question = cur.execute("select * from question where position =" + position)

    
    #Exécution de la requete
    execdb(db_connection)

    response = question.fetchall()

    print(response)

    closeCursor(cur, db_connection)
    return response

def PutQuestion(position_id, questionObject):
	#Connexion à la base de données
	cur, db_connection = connectdb()

	#Formatage des valeurs
	title = questionObject.title.replace("'", "\'")
	text = questionObject.text.replace("'", "\'")
	position = questionObject.position
	image = questionObject.image.replace("'", "\'")

	#Requete de modification des questions en base de données
	update_result = cur.execute(
        f'update question SET position = "{position}", text = "{text}", title = "{title}", image = "{image}" where position = "{position_id}"'
	)

	#Exécution de la requete
	execdb(db_connection)

	closeCursor(cur, db_connection)
	return True

def PutAnswer(answerObject):
	#Question sont supprimés avant l'ajout en base
	insertAnswer(answerObject)
	
	
def getAnswer(position):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Requete de récupération des questions en base de données
    question = cur.execute("select * from answer where question_position =" + position)

    
    #Exécution de la requete
    execdb(db_connection)

    response = question.fetchall()

    print(response)

    closeCursor(cur, db_connection)
    return response


def insertAnswer(answerObject):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Formatage des valeurs
    isCorrect = answerObject.isCorrect
    text = answerObject.text.replace("'", "\'")
    question_position = answerObject.question

    #Requete d'insertion de question en base de données
    insertion_result = cur.execute(
        f"insert into answer (is_correct, text, question_position) values"
        f'("{isCorrect}", "{text}", "{question_position}")')

    #Exécution de la requete
    execdb(db_connection)

    closeCursor(cur, db_connection)