import json
from json import JSONEncoder

class Participant:
	def __init__(self,playerName, score, answersSummaries):
		self.playerName = playerName
		self.score = score
		self.answersSummaries = answersSummaries
		

# subclass JSONEncoder
class ParticipantEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__