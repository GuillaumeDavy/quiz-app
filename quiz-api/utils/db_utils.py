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

def incrementQuestionLessThanPosition(position):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Requete de modification des questions en base de données
    increment_question = cur.execute(
        f"update question set position = position + 1 where position < {position} AND position > 0")

    #Exécution de la requete
    execdb(db_connection)

    closeCursor(cur, db_connection)

def decrementQuestion(position):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Requete de modification des questions en base de données
    increment_question = cur.execute(
        f"update question set position = position - 1 where position >= {position}")

    #Exécution de la requete
    execdb(db_connection)

    closeCursor(cur, db_connection)

def incrementAnswerLessThanPosition(position):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Requete de modification des questions en base de données
    increment_answer = cur.execute(
        f"update answer set question_position = question_position + 1 where question_position < {position} AND question_position > 0")

    #Exécution de la requete
    execdb(db_connection)

    closeCursor(cur, db_connection)

def decrementAnswer(position):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Requete de modification des questions en base de données
    increment_answer = cur.execute(
        f"update answer set question_position = question_position - 1 where question_position >= {position}")

    #Exécution de la requete
    execdb(db_connection)

    closeCursor(cur, db_connection)
    

def insertQuestion(input_question):
	previousQuestion = getQuestion(input_question.position)
	if len(previousQuestion) > 0:
		previousQuestionPosition = previousQuestion[0][0]
		print(previousQuestionPosition)
		incrementAnswer(previousQuestionPosition)
		incrementQuestion(previousQuestionPosition)

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

def incrementQuestion(position):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Requete de modification des questions en base de données
    increment_question = cur.execute(
        f"update question set position = position + 1 where position >= {position}")

    #Exécution de la requete
    execdb(db_connection)

    closeCursor(cur, db_connection)

def incrementAnswer(position):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Requete de modification des questions en base de données
    increment_answer = cur.execute(
        f"update answer set question_position = question_position + 1 where question_position >= {position}")

    #Exécution de la requete
    execdb(db_connection)

    closeCursor(cur, db_connection)

def getQuestion(position):
    #Connexion à la base de données
    cur, db_connection = connectdb()

    #Requete de récupération des questions en base de données
    question = cur.execute("select position, text, title, image from question where position =" + str(position))

    
    #Exécution de la requete
    execdb(db_connection)

    response = question.fetchall()
    closeCursor(cur, db_connection)
    return response

def PutQuestion(position_id, questionObject):

	currentPosition = getQuestion(position_id)
	
	if(int(position_id) > questionObject.position):
		#Je met à 0 la question et les answers que je souhaite déplacer
		updatePositionQuestionTo0(position_id)
		updatePositionAnswerTo0(position_id)
		
		#J'incrémente les questions et les inférieures à celle que je déplace
		incrementQuestionLessThanPosition(position_id)
		
		#J'incrémente les réponses inférieures à celle que je déplace
		incrementAnswerLessThanPosition(position_id)

		#Je place la question et les réponses au bon emplacement
		updatePositionQuestion(0, questionObject)
		updatePositionAnswer(0, questionObject)
	elif(int(position_id) < questionObject.position):
		#Je decrement celles qui sont supérieurs à celle que je déplace
		decrementQuestion(questionObject.position)
		decrementAnswer(questionObject.position)
	elif(int(position_id) == questionObject.position):
		return updateCompleteQuestion(position_id, questionObject)

def updatePositionQuestionTo0(position_id):
	#Connexion à la base de données
	cur, db_connection = connectdb()

	#Requete de modification des questions en base de données
	update_question = cur.execute(
		f"update question set position = 0 where position = {position_id}")

	#Exécution de la requete
	execdb(db_connection)

	closeCursor(cur, db_connection)

def updatePositionAnswerTo0(position_id):
	#Connexion à la base de données
	cur, db_connection = connectdb()

	#Requete de modification des questions en base de données
	update_question = cur.execute(
		f"update answer set question_position = 0 where question_position = {position_id}")

	#Exécution de la requete
	execdb(db_connection)

	closeCursor(cur, db_connection)


def updatePositionQuestion(position_id, questionObject):
	#Connexion à la base de données
	cur, db_connection = connectdb()

	#Formatage des valeurs
	title = questionObject.title.replace("'", "\'")
	text = questionObject.text.replace("'", "\'")
	position = questionObject.position
	image = questionObject.image.replace("'", "\'")


	#Requete de modification des questions en base de données
	update_question = cur.execute(
		f"update question set position = {position} where position = {position_id}")

	#Exécution de la requete
	execdb(db_connection)

	closeCursor(cur, db_connection)

def updatePositionAnswer(position_id, questionObject):
	#Connexion à la base de données
	cur, db_connection = connectdb()

	position = questionObject.position

	#Requete de modification des questions en base de données
	update_question = cur.execute(
		f"update answer set question_position = {position} where question_position = {position_id}")

	#Exécution de la requete
	execdb(db_connection)

	closeCursor(cur, db_connection)


def updateCompleteQuestion(position_id, questionObject):
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
    question = cur.execute("select * from answer where question_position =" + str(position))

    
    #Exécution de la requete
    execdb(db_connection)

    response = question.fetchall()


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