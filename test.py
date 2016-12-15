#coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
basedir=os.path.abspath(os.path.dirname(__file__))
app=Flask(__name__)
db=SQLAlchemy(app)

class Role(db.Model):
    """
    角色
    """
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    users=db.relationship('User',backref='role',uselist=True)

    def __repr__(self):
        return '<Role %s>'%self.name

class Identification(db.Model):
    """
    身份证
    """
    __tablename__='idents'
    id=db.Column(db.Integer,primary_key=True)
    address=db.Column(db.String(64),unique=True)
    #user=db.relationship('User',backref='ident',uselist=False)

    def __repr__(self):
        return '<Identification %s>'%self.id

class User(db.Model):
    """
    用户
    """
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    #ident_id=db.Column(db.Integer,db.ForeignKey('idents.id'))
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    

    def __repr__(self):
        return '<User %s>'%self.name

relation=db.Table('relations',db.Column('student_id',db.Integer,db.ForeignKey('students.id')),db.Column('class_id',db.Integer,db.ForeignKey('classes.id')))


class Student(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    classes=db.relationship('Class',secondary=relation,backref=db.backref('students',lazy='dynamic'),lazy='dynamic')
    
    def __repr__(self):
        return '<Student %s>'%self.name

class Class(db.Model):
    __tablename__='classes'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)

    def __repr__(self):
        return '<CLass %s>'%self.name
