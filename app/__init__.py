from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
import string

app = Flask(__name__) #Creates the application object
app.config['MONGOALCHEMY_DATABASE'] = 'store_collection'
app.config['SECRET_KEY'] = 'no secrets, right!'
app.config['DEBUG'] = True
db = MongoAlchemy(app)

# Flask BCrypt will be used to salt the user password
flask_bcrypt = Bcrypt(app)

# Associate Flask-Login manager with current app
login_manager = LoginManager()
login_manager.init_app(app)

from app import routes #imports routes modules
from app import auth
