# Ce fichier contiens toutes les fonctions de base de données 
# permettant de modifier l'ordonnancement des questions.
# Il est inclu dans le fichier db_utils.py

from utils import db_helpers as db

def incrementQuestionLessThanPosition(position, question_position):
    #Connexion à la base de données
    cur, db_connection = db.connectdb()

    #Requete de modification des questions en base de données
    increment_question = cur.execute(
        f"update question set position = position + 1 where position < {position} AND position >= {question_position} AND position > 0")

    #Exécution de la requete
    db.execdb(db_connection)

    db.closeCursor(cur, db_connection)

def decrementQuestionLessThanPosition(position, question_position):
    #Connexion à la base de données
    cur, db_connection = db.connectdb()

    #Requete de modification des questions en base de données
    increment_question = cur.execute(
        f"update question set position = position - 1 where position > {position} AND position <= {question_position}")

    #Exécution de la requete
    db.execdb(db_connection)

    db.closeCursor(cur, db_connection)

def decrementQuestion(position):
    #Connexion à la base de données
    cur, db_connection = db.connectdb()

    #Requete de modification des questions en base de données
    increment_question = cur.execute(
        f"update question set position = position - 1 where position >= {position}")

    #Exécution de la requete
    db.execdb(db_connection)

    db.closeCursor(cur, db_connection)

def incrementAnswerLessThanPosition(position, answer_position):
    #Connexion à la base de données
    cur, db_connection = db.connectdb()

    #Requete de modification des questions en base de données
    increment_answer = cur.execute(
        f"update answer set question_position = question_position + 1 where question_position < {position} AND question_position >= {answer_position} AND question_position > 0")

    #Exécution de la requete
    db.execdb(db_connection)

    db.closeCursor(cur, db_connection)

def decrementAnswerLessThanPosition(position, answer_position):
    #Connexion à la base de données
    cur, db_connection = db.connectdb()

    #Requete de modification des questions en base de données
    increment_answer = cur.execute(
        f"update answer set question_position = question_position - 1 where question_position > {position} AND question_position <= {answer_position}")

    #Exécution de la requete
    db.execdb(db_connection)

    db.closeCursor(cur, db_connection)

def decrementAnswer(position):
    #Connexion à la base de données
    cur, db_connection = db.connectdb()

    #Requete de modification des questions en base de données
    increment_answer = cur.execute(
        f"update answer set question_position = question_position - 1 where question_position >= {position}")

    #Exécution de la requete
    db.execdb(db_connection)

    db.closeCursor(cur, db_connection)


def incrementQuestion(position):
    #Connexion à la base de données
    cur, db_connection = db.connectdb()

    #Requete de modification des questions en base de données
    increment_question = cur.execute(
        f"update question set position = position + 1 where position >= {position}")

    #Exécution de la requete
    db.execdb(db_connection)

    db.closeCursor(cur, db_connection)

def incrementAnswer(position):
    #Connexion à la base de données
    cur, db_connection = db.connectdb()

    #Requete de modification des questions en base de données
    increment_answer = cur.execute(
        f"update answer set question_position = question_position + 1 where question_position >= {position}")

    #Exécution de la requete
    db.execdb(db_connection)

    db.closeCursor(cur, db_connection)



def updatePositionQuestionTo0(position_id):
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

	#Requete de modification des questions en base de données
	update_question = cur.execute(
		f"update question set position = 0 where position = {position_id}")

	#Exécution de la requete
	db.execdb(db_connection)

	db.closeCursor(cur, db_connection)

def updatePositionAnswerTo0(position_id):
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

	#Requete de modification des questions en base de données
	update_question = cur.execute(
		f"update answer set question_position = 0 where question_position = {position_id}")

	#Exécution de la requete
	db.execdb(db_connection)

	db.closeCursor(cur, db_connection)


def updatePositionQuestion(position_id, questionObject):
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

	#Formatage des valeurs
	title = questionObject.title.replace("'", "\'")
	text = questionObject.text.replace("'", "\'")
	position = questionObject.position
	image = questionObject.image.replace("'", "\'")


	#Requete de modification des questions en base de données
	update_question = cur.execute(
		f"update question set position = {position} where position = {position_id}")

	#Exécution de la requete
	db.execdb(db_connection)

	db.closeCursor(cur, db_connection)

def updatePositionAnswer(position_id, questionObject):
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

	position = questionObject.position

	#Requete de modification des questions en base de données
	update_question = cur.execute(
		f"update answer set question_position = {position} where question_position = {position_id}")

	#Exécution de la requete
	db.execdb(db_connection)

	db.closeCursor(cur, db_connection)

