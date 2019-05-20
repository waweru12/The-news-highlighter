from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class LoginForm(FlaskForm):
    '''
    '''
    username = StringField('User Name', validators=[Required()])
    password = TextAreaField('Password', validators=[Required()])
    submit = SubmitField('login')