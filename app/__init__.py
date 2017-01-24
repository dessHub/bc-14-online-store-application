from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy
import string

app = Flask(__name__) #Creates the application object
app.config['MONGOALCHEMY_DATABASE'] = 'store_collection'
app.config['SECRET_KEY'] = 'no secrets, right!'
app.config['DEBUG'] = True
db = MongoAlchemy(app)

from app import routes #imports routes modules
