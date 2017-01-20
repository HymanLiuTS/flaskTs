#!/usr/bin/env python  
import os  
from app import create_app,db  
from app.models import User,Role,create_roles,Post
from flask_script import Manager,Shell  
from flask_migrate import Migrate,MigrateCommand  
  
app=create_app(os.getenv('FLASK_CONFIG') or'default')  
manager=Manager(app)  
migrate=Migrate(app,db)  
  
def make_shell_context():  
    return dict(app=app,db=db,User=User,Role=Role,Post=Post,create_roles=create_roles)  
  
manager.add_command("shell",Shell(make_context=make_shell_context))  
manager.add_command('db',MigrateCommand)  

COV=None
if os.environ.get('COVERAGE'):
    import coverage
    COV=coverage.coverage(branch=True,include='app/*')
    COV.start()
 
@manager.command  
def test(coverage=False):  
    """Run the unit tests""" 
    if coverage and not os.environ.get('COVERAGE'):
        import sys
        os.environ['COVERAGE']='1'
        os.execvp(sys.executable,[sys.executable]+sys.argv) 
    import unittest  
    tests=unittest.TestLoader().discover('tests')  
    unittest.TextTestRunner(verbosity=2).run(tests)  
    if COV:
        COV.stop()
        COV.save()
        print('Coverage:')
        COV.report()
        COV.erase()
 
@manager.command  
def myprint():  
    print 'hello world'  
  
if __name__=='__main__':  
    manager.run()  
