#coding:utf-8
from flask import Flask,session,make_response,redirect,abort,request,render_template
from flask_script import Manager
import datetime
app=Flask(__name__)
manager=Manager(app)


class Myobj(object):
    def __init__(self,name):
        self.name=name

    def getname(self):
        return self.name



@app.route('/')
def index():
    mydict={'key1':'123','key':'hello'}
    mylist=(123,234,345,789)
    myintvar=0
    myobj=Myobj('Hyman')
    return render_template('param.html',mydict=mydict,mylist=mylist,myintvar=0,myobj=myobj)

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


@app.route('/if')
def iffunc():
    return render_template('if.html')

@app.route('/for')
def forfunc():
    comments=['nihao','123','asd','zxc']
    return render_template('for.html',comments=comments)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

if __name__=='__main__':
    manager.run()


