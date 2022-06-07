from utils import db_helpers as db
from utils import db_reordering as db_reordering
    

def insertQuestion(input_question):
	previousQuestion = getQuestion(input_question.position)
	if len(previousQuestion) > 0:
		previousQuestionPosition = previousQuestion[0][0]
		print(previousQuestionPosition)
		db_reordering.incrementAnswer(previousQuestionPosition)
		db_reordering.incrementQuestion(previousQuestionPosition)

	#Connexion à la base de données
	cur, db_connection = db.connectdb()

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
	db.execdb(db_connection)

	db.closeCursor(cur, db_connection)

def deleteQuestion(position):
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

	#Requete de suppression de question en base de données
	deletion_result = cur.execute(
		f"delete from question where position = '{position}'")

	#Exécution de la requete
	db.execdb(db_connection)

	db.closeCursor(cur, db_connection)
	db_reordering.decrementQuestion(position)
	

def deleteAnswer(position):

    #Connexion à la base de données
	cur, db_connection = db.connectdb()

    #Requete de suppression de question en base de données
	deletion_result = cur.execute(
        f"delete from answer where question_position = '{position}'")

    #Exécution de la requete
	db.execdb(db_connection)

	db.closeCursor(cur, db_connection)
	db_reordering.decrementAnswer(position)

def getQuestion(position):
    #Connexion à la base de données
    cur, db_connection = db.connectdb()

    #Requete de récupération des questions en base de données
    question = cur.execute("select position, text, title, image from question where position =" + str(position))

    
    #Exécution de la requete
    db.execdb(db_connection)

    response = question.fetchall()
    db.closeCursor(cur, db_connection)
    return response

def countQuestions():
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

	#Requete de récupération des questions en base de données
	question = cur.execute("select count(*) from question")

	
	#Exécution de la requete
	db.execdb(db_connection)

	response = question.fetchall()
	db.closeCursor(cur, db_connection)
	return response

def reorderQuestions(position_id, questionObject):
	# Si je déplace la question vers le haut
	if(int(position_id) > questionObject.position):
		#Je met à 0 la question et les answers que je souhaite déplacer
		db_reordering.updatePositionQuestionTo0(position_id)
		db_reordering.updatePositionAnswerTo0(position_id)
		
		#J'incrémente les questions inférieures à celle que je déplace
		db_reordering.incrementQuestionLessThanPosition(position_id, questionObject.position)
		
		#J'incrémente les réponses inférieures à celle que je déplace
		db_reordering.incrementAnswerLessThanPosition(position_id, questionObject.position)

		#Je place la question et les réponses au bon emplacement
		db_reordering.updatePositionQuestion(0, questionObject)
		db_reordering.updatePositionAnswer(0, questionObject)
		return True

	#Si je déplace la question vers le bas
	elif(int(position_id) < questionObject.position):
		#Je met à 0 la question et les answers que je souhaite déplacer
		db_reordering.updatePositionQuestionTo0(position_id)
		db_reordering.updatePositionAnswerTo0(position_id)
		
		#Je décrémente les questions supérieurs à celle que je déplace
		db_reordering.decrementQuestionLessThanPosition(position_id, questionObject.position)
		
		#J'incrémente les réponses supérieurs à celle que je déplace
		db_reordering.decrementAnswerLessThanPosition(position_id, questionObject.position)

		#Je place la question et les réponses au bon emplacement
		db_reordering.updatePositionQuestion(0, questionObject)
		db_reordering.updatePositionAnswer(0, questionObject)
		return True


def PutQuestion(position_id, questionObject):
	
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

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
	db.execdb(db_connection)

	db.closeCursor(cur, db_connection)
	return True

def updateCompleteQuestion(position_id, questionObject):
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

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
	db.execdb(db_connection)

	db.closeCursor(cur, db_connection)
	return True

def PutAnswer(answerObject, answerId):
	 
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

	#Formatage des valeurs
	isCorrect = answerObject.isCorrect
	text = answerObject.text.replace("'", "\'")
	question_position = answerObject.question

	#Requete de modification des questions en base de données
	update_result = cur.execute(
		f'update answer SET question_position = "{question_position}", text = "{text}", is_correct = "{isCorrect}" where answer_id = "{answerId}"'
	)

	#Exécution de la requete
	db.execdb(db_connection)

	db.closeCursor(cur, db_connection)
	return True
	
	
def getAnswer(position):
    #Connexion à la base de données
    cur, db_connection = db.connectdb()

    #Requete de récupération des questions en base de données
    question = cur.execute("select * from answer where question_position =" + str(position))

    
    #Exécution de la requete
    db.execdb(db_connection)

    response = question.fetchall()


    db.closeCursor(cur, db_connection)
    return response


def insertAnswer(answerObject):
    #Connexion à la base de données
    cur, db_connection = db.connectdb()

    #Formatage des valeurs
    isCorrect = answerObject.isCorrect
    text = answerObject.text.replace("'", "\'")
    question_position = answerObject.question

    #Requete d'insertion de question en base de données
    insertion_result = cur.execute(
        f"insert into answer (is_correct, text, question_position) values"
        f'("{isCorrect}", "{text}", "{question_position}")')

    #Exécution de la requete
    db.execdb(db_connection)

    db.closeCursor(cur, db_connection)

def insertParticipant(participantObject):
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

	#Formatage des valeurs
	name = participantObject.playerName.replace("'", "\'")

	#Requete d'insertion de question en base de données
	cur.execute(
		f"insert into participant (name) values"
		f'("{name}")')

	#Exécution de la requete
	db.execdb(db_connection)

	db.closeCursor(cur, db_connection)

def getLastParticipant():
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

	#Requete de récupération des questions en base de données
	question = cur.execute("select * from participant order by id desc limit 1")

	#Exécution de la requete
	db.execdb(db_connection)

	response = question.fetchall()

	db.closeCursor(cur, db_connection)
	return response

def getAllParticipants():
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

	#Requete de récupération des questions en base de données
	question = cur.execute("select * from participant ")

	#Exécution de la requete
	db.execdb(db_connection)

	response = question.fetchall()

	db.closeCursor(cur, db_connection)
	return response

def getParticipantAnswersById(participantId):
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

	#Requete de récupération des questions en base de données
	question = cur.execute("select * from participant_answers where id_participant = " + str(participantId))

	#Exécution de la requete
	db.execdb(db_connection)

	response = question.fetchall()

	db.closeCursor(cur, db_connection)
	return response

def getIdParticipantByName(participantName):
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

	#Requete de récupération des questions en base de données
	question = cur.execute(f"select id from participant where name = '{participantName}'")

	#Exécution de la requete
	db.execdb(db_connection)

	response = question.fetchall()

	db.closeCursor(cur, db_connection)
	return response

def insertParticipantAnswer(participantId, answerPosition):

	#Connexion à la base de données
	cur, db_connection = db.connectdb()

	#Requete d'insertion de question en base de données
	cur.execute(
		f"insert into participant_answers (id_participant, answer) values"
		f'("{participantId}", "{answerPosition}")')

	#Exécution de la requete
	db.execdb(db_connection)

	db.closeCursor(cur, db_connection)


def deleteAllParticipantsAndAnswers():
	#Connexion à la base de données
	cur, db_connection = db.connectdb()

	#Requete de suppression de question en base de données
	cur.execute(
		f"delete from participant "
	)
	cur.execute(
		f"delete from participant_answers "
	)

	#Exécution de la requete
	db.execdb(db_connection)

	db.closeCursor(cur, db_connection)