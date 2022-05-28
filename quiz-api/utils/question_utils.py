from asyncio.windows_events import NULL
from contextlib import nullcontext
import json
from queue import Empty
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
    # check is quest is empty
    if not checkQuestionPosition(position):
        return False

    db_utils.deleteQuestion(position)
    db_utils.deleteAnswer(position)
    
    return True

def checkQuestionPosition(position):
    quest = db_utils.getQuestion(position)
    # check is quest is empty
    if not quest:
        return False
    return True

def Get(position):
    quest = db_utils.getQuestion(position)
    # check is quest is empty
    if not checkQuestionPosition(position):
        return False

   
    
    answers = []
    ans = db_utils.getAnswer(position)

    #Je boucle sur le nombre de résultats de la fonction getanswer
    for i in range(len(db_utils.getAnswer(position))):

        isCorrect = ans[i][2]
        text = ans[i][1]
        question = ans[i][3]

        answers.append(a.Answer(True if isCorrect == "True" else False, text, question))
    
    title = quest[0][2]
    text = quest[0][1]
    position = quest[0][0]
    image = quest[0][3]

    question = q.Question(title, text, position, image, answers)
    questionJSONData = json.dumps(question, indent=4, cls=q.QuestionEncoder)
    return json.loads(questionJSONData)

def Put(position, question_json):
    if not checkQuestionPosition(position):
        return False
        
    quest = q.Question(question_json['title'], question_json['text'], question_json['position'], question_json['image'], [] )
    #Put des questions
    ans.Put(question_json, position)

    #Put des questions
    db_utils.PutQuestion(position, quest)
    return True