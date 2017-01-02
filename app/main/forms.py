from flask_wtf import FlaskForm  
from wtforms import TextField,SubmitField,PasswordField  
from wtforms.validators import DataRequired  
  
class NameForm(FlaskForm):  
    name=TextField('what is your name?',validators=[DataRequired()])  
    password=PasswordField('what is your password?',validators=[DataRequired()])
    login=SubmitField('login')
    logout=SubmitField('logout')
