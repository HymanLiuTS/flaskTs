from flask_wtf import FlaskForm  
from wtforms import TextField,SubmitField  
from wtforms.validators import DataRequired  
  
class NameForm(FlaskForm):  
    name=TextField('what is your name?',validators=[DataRequired()])  
    submit=SubmitField('Submit') 
