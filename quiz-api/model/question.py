import json
from json import JSONEncoder

class Question:
	def __init__(self,title, text, position, image, answer):
		self.title = title
		self.text = text
		self.position = position
		self.image = image
		self.possibleAnswers = answer

# subclass JSONEncoder
class QuestionEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__