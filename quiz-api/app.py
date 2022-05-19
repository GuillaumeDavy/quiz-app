from asyncio.windows_events import NULL
from flask import Flask, request, json
from utils import question_utils as qs, jwt_utils as jwt
app = Flask(__name__)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200


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
		token.split(' ')[1]
	else:
		return 'No token provided', 401

	if is_valid_token(token):
		qs.Delete(position)
		return 'Success', 200
	else:
		return 'Token is invalid', 401

@app.route('/questions/<position>', methods=['GET'])
def GetQuestion(position):
	#Maybe return in json format here
	return qs.Get(position)


def is_valid_token(token):
	return jwt.decode_token(token)

		
if __name__ == "__main__":
    app.run(ssl_context='adhoc')