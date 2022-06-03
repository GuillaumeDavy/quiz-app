from asyncio.windows_events import NULL
from contextlib import nullcontext
import json
from queue import Empty
from types import SimpleNamespace
from model import question as q
from model import answer as a
from utils import db_utils
from utils import answer_utils as ans
from utils.participant_utils import obj_dict

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
	
	quest = q.Question(question_json['title'], question_json['text'], question_json['position'], question_json['image'], [])

	#Put des questions
	db_utils.PutQuestion(position, quest)

	#Si la modification ne comporte pas de changement de position <-- BUG dans le cas ou il y a changement de position + de contenu
	if(int(position) == int(question_json["position"])):
		#Put des Answers
		ans.Put(question_json, position)

	return True

def GetAll():
	questionsToReturn = []
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
		questionsToReturn.append(json.loads(json.dumps(question, indent=4, cls=q.QuestionEncoder)))
	questionJSONData = json.dumps(questionsToReturn,default=obj_dict)
	print(questionJSONData)
	return questionJSONData

def obj_dict(obj):
    return obj.__dict__