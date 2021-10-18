from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('title', validators = [DataRequired()])
    description = StringField('description', validators = [DataRequired()])
    done = BooleanField('done')




