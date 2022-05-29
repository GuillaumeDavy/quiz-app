from asyncio.windows_events import NULL
from contextlib import nullcontext
import json
from queue import Empty
from types import SimpleNamespace
from model import question as q
from model import quizInfo as qi
from model import scores as s
from model import participant as p
from model import answersSummaries as ansSum
from utils import db_utils
from utils import answer_utils as ans

def Get():
	#On récupère le nombre de question total
	questionsNumber = db_utils.countQuestions()
	# On récupère tous les participants
	participants = db_utils.getAllParticipants()
	quizInfo = qi.quizInfo(questionsNumber[0][0], [])
	temp = []
	for participant in participants:
		i=1
		score = 0
		idParticipant = participant[0]
		participantAnswers = db_utils.getParticipantAnswersById(idParticipant)
		participantJsonAnswer = []
		for participantAnswer in participantAnswers:
			participantJsonAnswer.append(participantAnswer[2])
		for userAnswers in participantJsonAnswer:
			answers = db_utils.getAnswer(i)

			if(answers[int(userAnswers)-1][2] == "True"):
				score = score + 1
			i=i+1
		temp.append(s.scores(participant[1], score))

	scores = sorted(temp, key=lambda s: s.score, reverse=True)
	for score in scores:
		quizInfo.scores.append(s.scores(score.playerName, score.score))




	return json.dumps(quizInfo, indent=4, cls=qi.quizInfoEncoder)

def takeSecond(elem):
    return elem[1]

def GetParticipant(participant_json):
	i=1
	score = 0
	idParticipant = db_utils.getIdParticipantByName(participant_json["playerName"])
	participantAnswers = db_utils.getParticipantAnswersById(idParticipant[0][0])
	
	participantJsonAnswer = []
	for participantAnswer in participantAnswers:
		participantJsonAnswer.append(participantAnswer[2])
	for userAnswers in participantJsonAnswer:
		answers = db_utils.getAnswer(i)

		if(answers[int(userAnswers)-1][2] == "True"):
			score = score + 1
		i=i+1

	finalJson = {
		'playerName': participant_json["playerName"],
		'score': score
	}
	return json.dumps(finalJson)
		

	
def Post(participant_json):
	questionNumber = db_utils.countQuestions()
	if(len(participant_json["answers"]) < questionNumber[0][0]):
		return 405
	if(len(participant_json["answers"]) > questionNumber[0][0]):
		return 406
	participant = p.Participant(participant_json["playerName"], 0, [])
	db_utils.insertParticipant(participant)
	lastParticipant = db_utils.getLastParticipant()
	idLastParticipant = lastParticipant[0][0]
	for answer in participant_json["answers"]:
		db_utils.insertParticipantAnswer(idLastParticipant, answer)
	return 200

def Delete():
	db_utils.deleteAllParticipantsAndAnswers()
	return True

def displayParticipantsInfos():
	participantsToReturn = []
	participants = db_utils.getAllParticipants()
	if len(participants) == 0:
		return json.loads('{"size": 0, "scores": []}')
	for participant in participants:
		i=1
		score = 0
		answersSummaries = []
		idParticipant = participant[0]
		participantAnswers = db_utils.getParticipantAnswersById(idParticipant)
		print(participantAnswers)
		participantJsonAnswer = []
		for participantAnswer in participantAnswers:
			participantJsonAnswer.append(participantAnswer[2])
		for userAnswers in participantJsonAnswer:
			isUserCorrect = False
			answers = db_utils.getAnswer(i)

			if(answers[int(userAnswers)-1][2] == "True"):
				score = score + 1
				isUserCorrect = True

			correctAnswerPosition = 0
			for answer in answers:
				if(answer[2] == "False"):
					correctAnswerPosition = correctAnswerPosition + 1
				else:
					answersSummaries.append(ansSum.answersSummaries(correctAnswerPosition, isUserCorrect))
			i=i+1
		test = p.Participant(participant[1], score, answersSummaries)
		participantsToReturn.append(json.loads(json.dumps(test, indent=4, cls=p.ParticipantEncoder)))
		# return json.dumps(test, indent=4, cls=p.ParticipantEncoder)
		json_string = json.dumps(participantsToReturn, default=obj_dict)

	# participantJSONData = json.dumps(participantsToReturn, indent=4, cls=p.ParticipantEncoder)
	return json_string

def obj_dict(obj):
    return obj.__dict__