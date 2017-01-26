from flask import Flask
from flask.ext.pymongo import PyMongo
from flask.ext.login import LoginManager


app = Flask(__name__)     #initializes the application
app.config.from_object('config')  #database configuration
db = PyMongo(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views
from app import auth
