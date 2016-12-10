#coding:utf-8
from flask import Flask,session,make_response,redirect,abort,request,render_template
from flask_script import Manager
from flask_moment import Moment
import datetime
app=Flask(__name__)
manager=Manager(app)
moment=Moment(app)

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


if __name__=='__main__':
    manager.run()


