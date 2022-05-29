import json
from json import JSONEncoder

class quizInfo:
	def __init__(self,size, scores):
		self.size = size
		self.scores = scores		

# subclass JSONEncoder
class quizInfoEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__