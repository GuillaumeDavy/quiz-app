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

def Put(question_json, position=0):
    #Delete des questions avant la réinsertion <-- mieux de le mettre dans db_utils 
    pos = position if position != 0 else question_json['position']
    db_utils.deleteAnswer(pos)

    #Réinsertion
    for answer in question_json['possibleAnswers']:
        answer_obj = a.Answer(answer['isCorrect'], answer['text'], pos)
        db_utils.PutAnswer(answer_obj)