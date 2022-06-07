import json
from types import SimpleNamespace
from model import answer as a
from utils import db_utils

"""
	Description:
		Ajoute les answers d'une question en base de données
	Entrée :
		Une question au format JSON
"""
def PostAnswer(question_json):
    for answer in question_json['possibleAnswers']:
        answer_obj = a.Answer(answer['isCorrect'], answer['text'], question_json['position'])
        db_utils.insertAnswer(answer_obj)

"""
	Description:
		Modifie les answers d'une question en base de données
	Entrée :
        Une question au format JSON (quesrion_json)
        Une position d'answer (position)
"""
def PutAnswers(question_json, position):

    answers = db_utils.getAnswer(position)
    i = 0
    for answer in question_json['possibleAnswers']:
        idAnswer = answers[i][0]
        answer_obj = a.Answer(answer['isCorrect'], answer['text'], position)
        db_utils.PutAnswer(answer_obj, idAnswer)
        i=i+1