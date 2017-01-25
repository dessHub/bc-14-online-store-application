import wtforms
from flask.ext import wtf
from wtforms import validators
from app import login_manager, flask_bcrypt

from document import Store, User

class StoreForm(wtf.Form):
    document_class = Store
    title = wtforms.TextField(validators=[validators.Required()])
    description = wtforms.TextField(validators=[validators.Required()])
    instance = None

    def __init__(self, document=None, *args, **kwargs):
        super(StoreForm, self).__init__(*args, **kwargs)
        if document is not None:
            self.instance = document
            self._copy_data_to_form()

    def _copy_data_to_form(self):
        self.title.data = self.instance.title
        self.description.data = self.instance.description

    def save(self):
        if self.instance is None:
            self.instance = self.document_class()
        self.instance.title = self.title.data
        self.instance.description = self.description.data
        self.instance.save()
        return self.instance


class RegistrationForm(wtf.Form):
    document_class = User

    username = wtforms.StringField('Username', [validators.Length(min=4, max=25)])
    email = wtforms.StringField('Email Address', [validators.Length(min=6, max=35)])
    password = wtforms.PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = wtforms.PasswordField('Repeat Password')

    instance = None

    def __init__(self, document=None, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        if document is not None:
            self.instance = document
            self._copy_data_to_form()

    def _copy_data_to_form(self):
        self.username.data = self.instance.username
        self.email.data = self.instance.email
        self.password.data = self.instance.password
        self.confirm.data = self.instance.confirm

    def save(self):
        if self.instance is None:
            self.instance = self.document_class()
        self.instance.username = self.username.data
        self.instance.email = self.email.data
        self.instance.password = self.password.data
        self.instance.confirm = self.confirm.data
        self.instance.save()
        return self.instance


class LoginForm(wtf.Form):
    document_class = User

    email = wtforms.StringField('Email',validators=[validators.Required()])
    password = wtforms.PasswordField('Password',validators=[validators.Required()])

    def __init__(self, document=None, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        if document is not None:
            self.instance = document
            self._copy_data_to_form()

    def _copy_data_to_form(self):
        self.email.data = self.instance.email
        self.password.data = self.instance.password

    def save(self):
        if self.instance is None:
            self.instance = self.document_class()
        self.instance.email = self.email.data
        self.instance.password = self.password.data
        self.instance.save()
        return self.instance
