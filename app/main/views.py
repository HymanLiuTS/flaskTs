from datetime import datetime  
from flask import flash,render_template,session,redirect,url_for,current_app,request,jsonify,url_for
from . import main  
from .forms import NameForm,RegisterForm,PostForm
from .. import db  
from ..models import User,Post
from ..email import send_email
from .. import mail  
from flask_login import login_user,logout_user,current_user,login_required
 
 
@main.route('/',methods=['GET','POST'])  
def index():  
    return render_template('index.html')  

@main.route('/login',methods=['GET','POST'])
def login():
    form=NameForm()
    user=User.query.filter_by(username=form.name.data).first()
    if form.validate_on_submit():
        if user is not None and user.confirm_password(form.password.data):
            if current_user.is_authenticated:
                logout_user()
                flash('User Logout')
            else:
                login_user(user,True)
                flash('User Login')
    return render_template('login.html',form=form)

@main.route('/loginrq',methods=['GET','POST'])
@login_required
def loginrq():
    return 'I''m a private url'

@main.route('/register',methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        user=User(username=form.name.data,password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        token=user.generate_token()
        send_email(form.email.data,'Confirm Account','mail/new_user',user=user,token=token)
        return redirect(url_for(main.index))
    return render_template('register.html',form=form)

@main.route('/confirm/<token>')
@login_required
def confirm(token):
    if not current_user.confirmed:
        if current_user.confirm(token):
            flash('Confirm succeed')
        else: 
            flash('Confirm fail')
    return redirect(url_for('main.register'))

@main.route('/post')
def post():
    form=PostForm()
    return render_template('post.html',form=form)

@main.route('/posts/',methods=['POST'])
def new_post():
    post=Post.from_json(request.json)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json())

@main.route('/posts/',methods=['GET'])
def get_posts():
    posts=Post.query.all()
    return jsonify({'posts':[post.to_json() for post in posts]})

@main.route('/posts/<int:id>',methods=['GET'])
def get_post(id):
    post=Post.query.get_or_404(id)
    return jsonify(post.to_json())

@main.route('/shutdown')
def serv_shutdown():
    shutdown=request.environ.get('werkzeug.server.shutdown')
    shutdown()
    return 'shuting down'
