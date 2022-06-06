import json
from types import SimpleNamespace
from model import answer as a
from utils import db_utils

def Post(question_json):
    for answer in question_json['possibleAnswers']:
        answer_obj = a.Answer(answer['isCorrect'], answer['text'], question_json['position'])
        db_utils.insertAnswer(answer_obj)

def Delete(position):
    db_utils.deleteQuestion(position)

def Get():
    return db_utils.getQuestions()

def Put(question_json, position):

    #Delete des questions avant la réinsertion <-- mieux de le mettre dans db_utils 

    answers = db_utils.getAnswer(position)
    #Réinsertion
    i = 0
    for answer in question_json['possibleAnswers']:
        idAnswer = answers[i][0]
        answer_obj = a.Answer(answer['isCorrect'], answer['text'], position)
        db_utils.PutAnswer(answer_obj, idAnswer)
        i=i+1