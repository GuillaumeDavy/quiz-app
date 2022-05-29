import json
from json import JSONEncoder

class scores:
	def __init__(self,playerName, score):
		self.playerName = playerName
		self.score = score		

# subclass JSONEncoder
class scoresEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

def __getitem__(self, item):
    return self.score