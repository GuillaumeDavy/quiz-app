from asyncio.windows_events import NULL
from contextlib import nullcontext
import json
from queue import Empty
from types import SimpleNamespace
from model import question as q
from model import participant as p
from model import answersSummaries as ansSum
from utils import db_utils
from utils import answer_utils as ans

def Get():
	participantsToReturn = []
	participants = db_utils.getAllParticipants()
	for participant in participants:
		i=1
		score = 0
		answersSummaries = []
		idParticipant = participant[0]
		participantAnswers = db_utils.getParticipantAnswers(idParticipant)
		print(participantAnswers)
		participantJsonAnswer = []
		for participantAnswer in participantAnswers:
			participantJsonAnswer.append(participantAnswer[2])
		for userAnswers in participantJsonAnswer:
			isUserCorrect = False
			answers = db_utils.getAnswer(i)

			if(answers[int(userAnswers)][2] == "True"):
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
def Post(participant_json):
	participant = p.Participant(participant_json["playerName"], 0, [])
	db_utils.insertParticipant(participant)
	lastParticipant = db_utils.getLastParticipant()
	idLastParticipant = lastParticipant[0][0]
	for answer in participant_json["answers"]:
		db_utils.insertParticipantAnswer(idLastParticipant, answer)
	return True

def Delete():
	db_utils.deleteAllParticipantsAndAnswers()
	return True