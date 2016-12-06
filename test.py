#coding:utf-8
from flask import Flask,request
app=Flask(__name__)
@app.route('/')
def index():
    user_agent = request.headers.get('User_Agent')
    return 'user_agent is %s'%user_agent
    
@app.route('/<name>')
def user(name):
    return 'hello %s'%name

if __name__=='__main__':
    app.run(debug=True)


