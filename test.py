#coding:utf-8
from flask import Flask,session,make_response,redirect,abort
from flask_script import Manager
app=Flask(__name__)
manager=Manager(app)

@app.route('/')
def index():
    return 'bad request',400

@app.route('/response1')
def response1():
    response=make_response('set cookies')
    response.set_cookie('hyman','123')
    return response

@app.route('/response2')
def response2():
    return redirect('http://www.baidu.com')

@app.route('/error')
def error():
    abort(404)

@manager.command
def print_str():
    print 'hello world'

if __name__=='__main__':
    manager.run()


