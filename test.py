#coding:utf-8
from flask import Flask,session,make_response,redirect,abort,request,render_template
from flask_script import Manager
import datetime
app=Flask(__name__)
manager=Manager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)


@app.route('/set_cookie')
def set_cookie():
    response=make_response('set_cookie');
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


@app.route('/del_cookie')
def del_cookie():
    response=make_response('delete cookie')
    response.set_cookie('Name','',expires=0)
    return response

@app.route('/del_cookie2')
def del_cookie2():
    response=make_response('delete cookie2')
    response.delete_cookie('Name')
    return response

if __name__=='__main__':
    manager.run()


