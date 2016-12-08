#coding:utf-8
from flask import Flask,session,make_response,redirect,abort

app=Flask(__name__)

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

if __name__=='__main__':
    app.run(debug=True)


