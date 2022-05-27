from contextlib import nullcontext
import json
from types import SimpleNamespace
from model import question as q
from model import answer as a
from utils import db_utils
from utils import answer_utils as ans

def Post(question_json):
    quest = q.Question(question_json['title'], question_json['text'], question_json['position'], question_json['image'], [] )
    db_utils.insertQuestion(quest)
    ans.Post(question_json)
    
def Delete(position):
    db_utils.deleteQuestion(position)

def Get(position):
    question = q.Question(db_utils.getQuestion(position)[0][2], db_utils.getQuestion(position)[0][1], db_utils.getQuestion(position)[0][0], db_utils.getQuestion(position)[0][3], [])
    
    answers = []
    #Je boucle sur le nombre de résultats de la fonction getanswer
    for i in range(len(db_utils.getAnswer(position))):
        answers.append(a.Answer(True if db_utils.getAnswer(position)[i][2] == "True" else False, db_utils.getAnswer(position)[i][1], db_utils.getAnswer(position)[i][3]))
    
    question.possibleAnswers = answers
    questionJSONData = json.dumps(question, indent=4, cls=q.QuestionEncoder)
    return json.loads(questionJSONData)