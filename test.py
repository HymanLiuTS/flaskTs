#coding:utf-8
from flask import Flask,session,make_response,redirect,abort,request,render_template,g
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


