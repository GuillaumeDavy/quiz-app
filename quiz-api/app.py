from asyncio.windows_events import NULL
from flask import Flask, request, json
from flask_cors import CORS
from utils import question_utils as qs, participant_utils as pa, jwt_utils as jwt
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"


@app.route('/login', methods=['POST'])
def Login():
	payload = request.get_json()
	if payload['password'].strip() == 'Vive l\'ESIEE !':
		print("password is correct")
		return json.jsonify(token=jwt.build_token())
	else:
		return 'Wrong password', 401
	
@app.route('/questions', methods=['POST'])
def PostQuestions():
	token = request.headers.get('Authorization')
	if token:
		token = token.split(' ')[1]
	else:
		return 'No token provided', 401
	
	if is_valid_token(token):
		question_json = request.get_json()
		qs.Post(question_json)
		return 'Success', 200
	else:
		return 'Token is invalid', 401

@app.route('/questions/<position>', methods=['DELETE'])
def DeleteQuestion(position):
	token = request.headers.get('Authorization')
	if token != None:
		token = token.split(' ')[1]
	else:
		return 'No token provided', 401

	if is_valid_token(token):
		if qs.Delete(position):
			return 'Success', 204
		else:
			return 'Question not found', 404
	else:
		return 'Token is invalid', 402

@app.route('/questions/<position>', methods=['GET'])
def GetQuestion(position):
	if qs.Get(position):
		return qs.Get(position), 200
	else:
		return 'Question not found', 404


@app.route('/questions/<position>', methods=['PUT'])
def PutQuestion(position):
	question_json = request.get_json()
	if qs.Put(position, question_json):
		return 'Success', 200
	else:
		return 'Question not found', 404

@app.route('/participations', methods=['POST'])
def PostParticipations():
	participant_json = request.get_json()
	returnValue = pa.Post(participant_json)
	if returnValue == 200:
		return pa.GetParticipant(participant_json), 200 
	elif returnValue == 405:
		return 'Pas assez de réponses', 400
	elif returnValue == 406:
		return 'Trop de réponses', 400


@app.route('/participations', methods=['DELETE'])
def DeleteParticipations():
	token = request.headers.get('Authorization')
	if token:
		token = token.split(' ')[1]
	else:
		return 'No token provided', 401
	
	if is_valid_token(token):
		if pa.Delete():
			return 'Success', 204
		else:
			return 'Delete error', 409
	else:
		return 'Token is invalid', 401


@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return pa.Get(), 200
	
@app.route('/check-token', methods=['GET'])
def CheckToken():
	token = request.get_json()
	return "1" if check_token_validity(token["token"]) else "0", 200
	
def check_token_validity(token):
	return jwt.isTokenValid(token)

def is_valid_token(token):
	return jwt.decode_token(token)

		
if __name__ == "__main__":
    app.run()