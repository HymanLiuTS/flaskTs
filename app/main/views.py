from datetime import datetime  
from flask import flash,render_template,session,redirect,url_for,current_app
from . import main  
from .forms import NameForm  
from .. import db  
from ..models import User  
from .. import mail  
from ..email import msg 
from flask_login import login_user,logout_user,current_user,login_required
 
 
@main.route('/',methods=['GET','POST'])  
def index():  
    form=NameForm()  
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.name.data).first()  
        if user is None:  
            user = User(username=form.name.data,password=form.password.data)  
            db.session.add(user)
            flash('add a user')
        else:
            if user.confirm_password(form.password.data) is True:
                flash('password is right')
            else:
                flash('password is not right')
    return render_template('index.html',form=form)  

@main.route('/login',methods=['GET','POST'])
def login():
    form=NameForm()
    user=User.query.filter_by(username=form.name.data).first()
    if form.validate_on_submit():
        if user is not None and user.confirm_password(form.password.data):
            if current_user.is_authenticated:
                logout_user()
                flash('User Logout')
            else:
                login_user(user,True)
                flash('User Login')
    return render_template('login.html',form=form)

@main.route('/loginrq',methods=['GET','POST'])
@login_required
def loginrq():
    return 'I''m a private url'
    
