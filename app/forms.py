import wtforms
from flask.ext import wtf
from wtforms import validators

from document import Store

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
