from flask import jsonify,request
from task import app,db
from task.models import Survey,Question,User
from task.schemas import surveys_schema,survey_schema
from marshmallow import  ValidationError
from flask_jwt_extended import  jwt_required, create_access_token


@app.route("/")
@jwt_required
def home():
    return jsonify({"home":"Home Page"})

@app.route("/register",methods=["POST"])
def register():
    email = request.form['email']
    test = User.query.filter_by(email=email).first()
    if test:
        return jsonify(message="User already exist"), 409
    else:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username,password=password,email=email)
        db.session.add(user)
        db.session.commit()
        return jsonify(message="User has been created"), 201

@app.route('/login',methods=['POST'])
def login():
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else:
        email = request.form['email']
        password = request.form['password']
    test = User.query.filter_by(email=email,password=password).first()
    if test:
        access_token = create_access_token(identity=email)
        return jsonify(message="Login Succeeded",access_token=access_token)
    else:
        return jsonify(message="Invalid Email or Password"), 401
    
@app.route("/survey")
def get_surveys():
    return jsonify({"surveys":surveys_schema.dump(Survey.query.all())})

@app.route("/survey",methods=['POST'])
@jwt_required
def add_survey():
    json_data = request.get_json()
    if not json_data:
        return jsonify({"message": "No input data provided"}), 400
    # Validate and deserialize input
    try:
        data = survey_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 422
    
    survey = Survey(name=data['name'],description=data['description'])
    db.session.add(survey)
    db.session.commit()
    if data.get('questions'):
        for q in data['questions']:
            q = Question(body=q['body'],survey_id=survey.id,note=q['note'])
            db.session.add(q)
    db.session.commit()
    return {"message": "Created new survey."},200