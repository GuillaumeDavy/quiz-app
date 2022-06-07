import json
from model import question as q
from model import answer as a
from utils import db_utils
from utils import answer_utils as ans
from utils import participant_utils as pa
"""
	Description:
		Ajoute une question en base de données
	Entrée :
		Une question au format JSON
	Sortie :	
"""
def PostQuestion(question_json):
	#Création de l'objet question en fonction du json
	quest = q.Question(question_json['title'], question_json['text'], question_json['position'], question_json['image'], [] )

	#Insertion de la question dans la base de données
	db_utils.insertQuestion(quest)

	#Insertion des réponses dans la base de données
	ans.PostAnswer(question_json)
	
	# Supprime les participations du quizz car une question à été ajoutée.
	pa.DeleteParticipations()


"""
	Description:
		Supprime une question en base de données
	Entrée :
		Une position de question
"""
def DeleteQuestion(position):
	# Vérifie si la question existe
	if not checkQuestionPosition(position):
		return False

	# Supprime la question
	db_utils.deleteQuestion(position)

	# Supprime les réponses associées à la question
	db_utils.deleteAnswer(position)
	
	# Supprime les participations du quizz car une question à été supprimée.
	pa.DeleteParticipations()
	return True


"""
	Description:
		Vérifie que la question existe à a position passée en paramètre
	Entrée :
		Une position de question
	Sortie :
		False si la question n'existe pas, True sinon
"""
def checkQuestionPosition(position):
	quest = db_utils.getQuestion(position)
	# Vérifie que getQuestion renvoie un résultat
	if not quest:
		return False
	return True

"""
	Description:
		Retroune la question à la position passé en paramètre
	Entrée :
		Une position de question
	Sortie :
		Une quesition au format JSON
"""
def GetQuestion(position):
	# Vérifie si la question existe
	if not checkQuestionPosition(position):
		return False

	quest = db_utils.getQuestion(position)
	ans = db_utils.getAnswer(position)
	answers = []

	#Je boucle sur le nombre de résultats de la fonction get1nswer(position)
	for i in range(len(ans)):

		isCorrect = ans[i][2]
		text = ans[i][1]
		question = ans[i][3]

		# Crée un objet Answer et je l'ajoute à la liste des réponses "answers"
		answers.append(a.Answer(True if isCorrect == "True" else False, text, question))
	
	# Formate les données
	title = quest[0][2]
	text = quest[0][1]
	position = quest[0][0]
	image = quest[0][3]

	# Création d'un objet Question 
	question = q.Question(title, text, position, image, answers)

	# Convertit l'objet en JSON
	questionJSONData = json.dumps(question, indent=4, cls=q.QuestionEncoder)

	return json.loads(questionJSONData)


"""
	Description:
		Modifie une question en base de données
	Entrée :
		Une position de question (position)
		Une question au format JSON (question_json)
"""
def PutQuestion(position, question_json):
	# Vérifie si la question existe
	if not checkQuestionPosition(position):
		return False
	
	# Création de l'objet question en fonction du json
	quest = q.Question(question_json['title'], question_json['text'], question_json['position'], question_json['image'], [])

	#Reordering des questions si la question a changé de position, en comparant l'ID de l'ulr et au json.position
	if int(question_json["position"]) != int(position):
		# Réordering des questions avant modification
		reorderQuestions(position, quest)
		
	# Update des questions et des réponses à la position json.position (Reorder ? --> Ok, no Reorder ? --> Ok )
	db_utils.PutQuestion(quest.position, quest)
	ans.PutAnswers(question_json, quest.position)

	return True

"""
	Description:
		Réarrange les questions en base de données
	Entrée :
		Une position de question (position)
		Une question au format JSON (question_json)
"""
def reorderQuestions(position, question):
	# Réordering des questions avant modification (PUT)
	db_utils.reorderQuestions(position, question)
	return True

"""
	Description:
		Retourne toutes les questions de la base de données
	Sortie: 
		La liste de toutes les questions de la base de données au format JSON
"""
def GetAllQuestions():

	questions = []
	size = db_utils.countQuestions()
	
	for i in range(size[0][0]):
		answers = []
		quest = db_utils.getQuestion(i+1)
		ans = db_utils.getAnswer(i+1)

		#Je boucle sur le nombre de résultats de la fonction getanswer
		for k in range(len(ans)):
			isCorrect = ans[k][2]
			text = ans[k][1]
			question = ans[k][3]

			answers.append(a.Answer(True if isCorrect == "True" else False, text, question))
	
		title = quest[0][2]
		text = quest[0][1]
		position = quest[0][0]
		image = quest[0][3]

		question = q.Question(title, text, position, image, answers)
		questions.append(json.loads(json.dumps(question, indent=4, cls=q.QuestionEncoder)))
	questionsJSONData = json.dumps(questions,default=obj_dict)
	return questionsJSONData

"""
	Description:
		Fonction utilitaire permettant de retourner une clé-valeur pour les objets JSON
		Utile en particulier pour les arrays d'objets
	Entrée: 
		Un objet JSON
"""
def obj_dict(obj):
    return obj.__dict__