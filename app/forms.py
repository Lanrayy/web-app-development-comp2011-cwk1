from flask_wtf import Form
from wtforms import IntegerField
from wtforms import TextField
from wtforms import TextAreaField
from wtforms import DateField
from wtforms import SubmitField

from wtforms.validators import DataRequired

class CalculatorForm(Form):
    title = TextField('title', validators=[DataRequired()])
    module_code = TextField('module_code', validators=[DataRequired()])
    deadline = DateField('deadine',  validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])

class ButtonForm(Form):
    submit = SubmitField('Submit')
