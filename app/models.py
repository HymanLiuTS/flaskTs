from app import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
class Role(db.Model):  
    __tablename__='role'  
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    users=db.relationship('User',backref='role',lazy='dynamic')
    def __repr__(self):
        return '<Role %r>'% self.name
      
class User(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'))
    hash_password=db.Column(db.String(28))

    def __repr__(self):
        return '<User %r>'% self.username

    @property
    def password(self):
        raise AttributeError('password cannot be read');

    @password.setter
    def password(self,password):
        self.hash_password=generate_password_hash(password)

    def confirm_password(self,password):
        return check_password_hash(self.hash_password,password)

from . import loginmanager
@loginmanager.user_loader
def load_user(id):
    return User.query.get(int(id))
