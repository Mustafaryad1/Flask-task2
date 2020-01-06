# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

app = Flask(__name__)


# data base config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
# schema
ma = Marshmallow(app)
# config jwt
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'wanna-secret'

from task import routes