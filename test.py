#coding:utf-8
#usr/bin/env
from flask import Flask,session,make_response,redirect,abort,request,render_template,g,url_for,flash
from flask_script import Manager
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
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
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    users=db.relationship('User',backref='role')

    def __repr__(self):
        return '<Role %s>'%self.name

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    age=db.Column(db.Integer)

    def __repr__(self):
        return '<User %s>'%self.name


class NameForm(FlaskForm):
    name = StringField('your name',validators=[Required(),])
    submit = SubmitField('Submit')


@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user is None:
            user=User(name=form.name.data)
            db.session.add(user)
        session['name']=form.name.data
        form.name.data=''
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session['name'])

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


