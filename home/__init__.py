from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SECRET_KEY']="registrationform_flask"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir, 'user.db')

db=SQLAlchemy(app)

login_manager=LoginManager(app)
from home import routes


