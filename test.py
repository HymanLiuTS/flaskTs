#coding:utf-8
from flask import Flask
from flask_mail import Mail
import os
basedir=os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.qq.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD']=os.environ.get('MAIL_PASSWORD')
mail=Mail(app)

