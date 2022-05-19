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