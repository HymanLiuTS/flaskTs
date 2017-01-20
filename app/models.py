from app import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,AnonymousUserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask import url_for

class Role(db.Model):  
    __tablename__='role'  
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    permission=db.Column(db.Integer)
    users=db.relationship('User',backref='role',lazy='dynamic')
    
    def __repr__(self):
        return '<Role %r>'% self.name

class Permission:
    FOLLOW=0x01
    COMMENT=0x02
    WRITE=0x04
    MANAGE_COMMENTS=0x08
    ADMIN=0x80



class User(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'))
    hash_password=db.Column(db.String(28))
    confirmed=db.Column(db.Boolean,default=False)
    
    def __init__(self,**kwargs):
        super(User,self).__init__(**kwargs)
        if self.role is None:
            if self.username == 'Hyman':
                self.role=Role.query.filter_by(permission=0x8f).first()
            if self.role is None:
                self.role=Role.query.filter_by(permission=0x07).first()
    
    def can(self,permission):
        return self.role is not None and (self.role.permission & permission) == permission

    def is_admin(self):
        return self.can(Permission.ADMIN)

    def generate_token(self,expiration=3600):
        s=Serializer('secret key',expiration)
        return s.dumps({'confirm':self.id})

    def confirm(self,token):
        s=Serializer('secret key')
        data=s.loads(token)
        if data.get('confirm')!=self.id:
            return False
        self.confirm = True
        db.session.add(self)
        return True

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

class AnonymousUser(AnonymousUserMixin):
    def can(self,permission):
        return False
    def is_admin(self):
        return False

from . import loginmanager
@loginmanager.user_loader
def load_user(id):
    return User.query.get(int(id))

loginmanager.anonymous_user=AnonymousUser

def create_roles():
    roles={'User':Permission.FOLLOW|Permission.COMMENT|Permission.WRITE,
            'Moderator':Permission.FOLLOW|Permission.COMMENT|Permission.WRITE|Permission.MANAGE_COMMENTS,
            'Admin':Permission.FOLLOW|Permission.COMMENT|Permission.WRITE|Permission.MANAGE_COMMENTS|Permission.ADMIN
            }
    for r in roles:
        print r
        role = Role.query.filter_by(name=r).first()
        if role is None:
            role=Role(name=r)
        role.permission=roles[r]
        db.session.add(role)
    db.session.commit()

from markdown import markdown
import bleach
class Post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer,primary_key=True)
    body=db.Column(db.Text)
    timestamp=db.Column(db.DateTime,index=True,default=datetime.utcnow)
    html_body=db.Column(db.Text)
    def to_json(self):
        json_post={
        'url':url_for('main.get_post',id=self.id,_external=True),
        'body':self.body,
        'html_body':self.html_body
        }
        return json_post
    
    @staticmethod
    def from_json(json_post):
        body=json_post.get('body')
        return Post(body=body)

    @staticmethod
    def on_body_change(target,value,oldvalue,initiator):
        allowed_tags=['a','ul','strong','p','h1','h2','h3']
        html_body=markdown(value,output_format='html')
        html_body=bleach.clean(html_body,tags=allowed_tags,strip=True)
        html_body=bleach.linkify(html_body)
        target.html_body=html_body

db.event.listen(Post.body,'set',Post.on_body_change)

