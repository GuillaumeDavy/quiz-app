import json
from json import JSONEncoder


class Answer:
	def __init__(self, is_correct, text, question):
		self.text = text
		self.isCorrect = is_correct
		self.question = question

# subclass JSONEncoder
class AnswerEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__