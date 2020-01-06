# -*- coding: utf-8 -*-
from datetime import datetime
from task import db


 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
 

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description =  db.Column(db.String(1000), nullable=False)
    start_date = db.Column(db.DateTime,default=datetime.utcnow)
    end_date = db.Column(db.DateTime,default=datetime.utcnow )

        
    def __repr__(self):
        return f"Survey:{self.name}"
    
   
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(1000), nullable=False)
    note = db.Column(db.String(120), nullable=False)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'),
                          nullable=False)
    survey = db.relationship('Survey',backref=db.backref('questions', 
                                                         lazy=True))
    def __repr__(self):
        return f"Question:{self.body}"

