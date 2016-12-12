#coding:utf-8
from flask import Flask,session,make_response,redirect,abort,request,render_template,g,url_for,flash
from flask_script import Manager
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
import os
basedir=os.path.abspath(os.path.dirname(__file__))


import datetime
app=Flask(__name__)
app.config['SECRET_KEY']='secret_key'
manager=Manager(app)
moment=Moment(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir+'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db=SQLAlchemy(app)

class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)

    def __repr__(self):
        return '<Role %s>'%self.name

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)

    def __repr__(self):
        return '<User %s>'%self.name


class NameForm(FlaskForm):
    name = StringField('your name',validators=[Required(),])
    submit = SubmitField('Submit')


@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name=session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('name has been changed')
            return redirect(url_for('index'))
        session['name']=form.name.data
        return render_template('index.html',form=form)
    return render_template('index.html',form=form)

@app.route('/set_cookie')
def set_cookie():
    response=make_response('Hello World');
    outdate=datetime.datetime.today() + datetime.timedelta(days=30)
    response.set_cookie('Name','Hyman',expires=outdate)
    return response

@app.route('/get_cookie')
def get_cookie():
    name=request.cookies.get('Name')
    return name

@app.route('/get_template')
def get_template():
    return render_template('test.html')

@app.route('/moment')
def get_moment():
    return render_template('moment.html')

@app.route('/test')
def test():
    return g.string

@app.before_first_request
def bf_first_request():
    g.string = 'before_first_request'

@app.before_request
def bf_request():
    g.string = 'before_request'

@app.after_request
def af_request(param):
    return param

@app.teardown_request
def td_request(param):
    return param

if __name__=='__main__':
    manager.run()


