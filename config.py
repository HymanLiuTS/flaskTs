import os  
basedir = os.path.abspath(os.path.dirname(__file__))  
  
class Config:  
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'  
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  
    FLASKY_MAIL_SUBJECT_PREFIX='[Flasky]'  
    FLASKY_MAIL_SENDER = '879651072@qq.com'  
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')  
    SQLALCHEMY_TRACK_MODIFICATIONS = True  
    @staticmethod  
    def init_app(app):  
        pass  
  
class DevelopmentConfig(Config):  
    DEBUG = True  
    MAIL_SERVER = 'smtp.qq.com'  
    MAIL_PORT = 587  
    MAIL_USE_TLS = True  
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or\
            'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')  
  
class TestingConfig(Config):  
    TESTING = False  
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or\
            'sqlite:///' + os.path.join(basedir,'data-test.sqlite')  
  
class ProductionConfig(Config):  
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or\
            'sqlite:///' + os.path.join(basedir,'data.sqlite')  
  
config={  
        'development':DevelopmentConfig,  
        'testing':TestingConfig,  
        'production':ProductionConfig,  
        'default':DevelopmentConfig  
        }  
