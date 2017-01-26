from flask.ext.wtf import Form
import wtforms
from flask.ext import wtf
from wtforms import validators
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
#from models import Store, User


class LoginForm(Form):
    """Login form to access writing and settings pages"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegistrationForm(Form):

    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

class StoreForm(Form):

    title = StringField('Store Title')
    description = StringField('Store Description')
    user_id = StringField('Your Username')

class ProductForm(Form):

    product_name = StringField('Product Title')
    description = StringField('Product Description')
    user_id = StringField('Your Username')
