from flask_mail import Message
from app import mail
from flask import render_template

def send_email(to,subject,template,**kwargs):
    msg=Message("[TecnologyDreamer]"+subject,sender='879651072@qq.com',recipients=[to])
    msg.body=render_template(template+'.txt',**kwargs)
    msg.html=render_template(template+'.html',**kwargs)
    mail.send(msg)
