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
	if payload['password'].strip() == 'Vive l\'ESIEE':
		print("password is correct")
		return json.jsonify(token=jwt.build_token())
	else:
		return 'Wrong password', 401
	
@app.route('/questions', methods=['POST'])
def PostQuestions():
	token = request.headers.get('Authorization')
	question_json = request.get_json()

	# TODO PARSER DECODER FOR QUESTION OBJECT
	qs.PostQuestion(question_json)
	return '', 200

@app.route('/questions/<id>', methods=['DELETE'])

def is_valid_token(token):
	return token is None or jwt.decode_token(token)

if __name__ == "__main__":
    app.run(ssl_context='adhoc')