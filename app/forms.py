from flask_wtf import Form
from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, EqualTo, Length

class PostForm(Form):
    post = StringField('post', validators=[DataRequired()])

class AddForm(Form):
    title = StringField('title', validators=[DataRequired()])
    text  = StringField('text', default=False)
    tags  = StringField('tags', default=False)