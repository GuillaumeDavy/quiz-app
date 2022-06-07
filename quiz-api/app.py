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

"""
	@Route: /login
	@Method: POST
	@Body: Token: <Token String>

	Description:
		Retourne un token si le mot de passe passé en body est correct
	Sortie: 
		Token au format JSON
"""
@app.route('/login', methods=['POST'])
def Login():
	payload = request.get_json()
	if payload['password'].strip() == 'Vive l\'ESIEE !':
		print("password is correct")
		return json.jsonify(token=jwt.build_token())
	else:
		return 'Wrong password', 401

"""
	@Route: /questions
	@Method: POST
	@Header: Authorization: Bearer <token>
	@Body: QuestionObject{}

	Description:
		Ajoute une question passée en body de la requête en base de données
"""
@app.route('/questions', methods=['POST'])
def PostQuestions():
	token = request.headers.get('Authorization')
	if token:
		token = token.split(' ')[1]
	else:
		return 'No token provided', 401
	
	if is_valid_token(token):
		question_json = request.get_json()
		qs.PostQuestion(question_json)
		return 'Success', 200
	else:
		return 'Token is invalid', 401

"""
	@Route: /questions/<position>
	@Method: DELETE
	@Header: Authorization: Bearer <token>

	Description:
		Supprime une question en base de données à la position passée en paramètre URL de la requête 
"""
@app.route('/questions/<position>', methods=['DELETE'])
def DeleteQuestion(position):
	token = request.headers.get('Authorization')
	if token != None:
		token = token.split(' ')[1]
	else:
		return 'No token provided', 401

	if is_valid_token(token):
		if qs.DeleteQuestion(position):
			return 'Success', 204
		else:
			return 'Question not found', 404
	else:
		return 'Token is invalid', 402

"""
	@Route: /questions/<position>
	@Method: GET

	Description:
		Retourne la question à la position passée en paramètre URL de la requête 	
	Sortie: 
		Question au format JSON, 200
"""
@app.route('/questions/<position>', methods=['GET'])
def GetQuestion(position):
	if qs.GetQuestion(position):
		return qs.GetQuestion(position), 200
	else:
		return 'Question not found', 404


"""
	@Route: /questions
	@Method: GET

	Description:
		Retourne toutes les questions de la base de données 	
	Sortie: 
		Questions au format JSON, 200
"""
@app.route('/questions', methods=['GET'])
def GetQuestions():
	if qs.GetAllQuestions():
		return qs.GetAllQuestions(), 200
	else:
		return 'Questions not found', 404

"""
	@Route: /questions/<position>
	@Method: PUT
	@Body: QuestionObject{}

	Description:
		Modifie la question à la position passée en paramètre URL de la requête par la question passée en body de la requête
"""
@app.route('/questions/<position>', methods=['PUT'])
def PutQuestion(position):
	question_json = request.get_json()
	if qs.PutQuestion(position, question_json):
		return 'Success', 200
	else:
		return 'Question not found', 404

"""
	@Route: /participations
	@Method: POST
	@Body: ParticipationObject{}

	Description:
		Ajoute une participation passée en body de la requête en base de données

	Sortie:
		Participation au format JSON, 200
"""
@app.route('/participations', methods=['POST'])
def PostParticipations():
	participant_json = request.get_json()
	returnValue = pa.PostParticipations(participant_json)
	if returnValue == 200:
		return pa.GetParticipant(participant_json), 200 
	elif returnValue == 405:
		return 'Pas assez de réponses', 400
	elif returnValue == 406:
		return 'Trop de réponses', 400

"""
	@Route: /participations
	@Method: DELETE
	@Header: Authorization: Bearer <token>

	Description:
		Supprime toutes les participations de la base de données
"""
@app.route('/participations', methods=['DELETE'])
def DeleteParticipations():
	token = request.headers.get('Authorization')
	if token:
		token = token.split(' ')[1]
	else:
		return 'No token provided', 401
	
	if is_valid_token(token):
		if pa.DeleteParticipations():
			return 'Success', 204
		else:
			return 'Delete error', 409
	else:
		return 'Token is invalid', 401

"""
	@Route: /quiz-info
	@Method: GET

	Description:
		Retourne les informations du quiz (participations)
	Sortie:
		Partiipations au format JSON, 200
"""
@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return pa.GetQuizInfo(), 200
	
"""
	@Route: /check-token
	@Method: POST
	@Body: TokenObject{}

	Description:
		Vérifie la validité du token passé en body de la requête
	Sortie:
		"1" si le token est valide, "0" sinon
"""
@app.route('/check-token', methods=['POST'])
def CheckToken():
	token = request.get_json()
	return "1" if check_token_validity(token["token"]) else "0", 200
	
def check_token_validity(token):
	return jwt.isTokenValid(token)

def is_valid_token(token):
	return jwt.decode_token(token)

		
if __name__ == "__main__":
    app.run()