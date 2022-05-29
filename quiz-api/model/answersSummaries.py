import json
from json import JSONEncoder

class answersSummaries:
	def __init__(self,correctAnswerPosition, wasCorrect):
		self.correctAnswerPosition = correctAnswerPosition
		self.wasCorrect = wasCorrect		

# subclass JSONEncoder
class answersSummariesEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__