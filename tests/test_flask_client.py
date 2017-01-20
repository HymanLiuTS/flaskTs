#coding:utf-8
import unittest
from flask import current_app,url_for,json
from app import create_app,db
class FlaskClientTest(unittest.TestCase):
    def setUp(self):
        self.app=create_app('testing')
        self.app_context=self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client=self.app.test_client()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_home_page(self):
        response=self.client.get(url_for('main.index'))
        self.assertTrue('Home' in response.get_data(as_text=True))
    
    def test_register(self):
        response=self.client.post(url_for('main.register'),data={
            'email':'879651072@qq.com',
            'name':'Hyman',
            'password1':'123',
            'password2':'123'})
        self.assertTrue(response.status_code==302)
    
    def test_posts(self):
        response=self.client.post(
            url_for('main.new_post'),
            data=json.dumps({'body':'I am a new post'}),
            content_type='application/json')
        self.assertTrue(response.status_code==200)
        
