import json
from types import SimpleNamespace
from model import question as q

def PostQuestion(question_json):

    a = q.Question(question_json['title'], question_json['text'], question_json['position'], question_json['image'])
    print(a)