import json
from types import SimpleNamespace
from model import question as q
from utils import db_utils
from utils import answer_utils as ans

def Post(question_json):
    quest = q.Question(question_json['title'], question_json['text'], question_json['position'], question_json['image'])
    db_utils.insertQuestion(quest)
    ans.Post(question_json)
    
def Delete(position):
    db_utils.deleteQuestion(position)

def Get():
    return db_utils.getQuestions()