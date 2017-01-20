#coding:utf-8
import unittest
from flask import current_app,url_for,json
from app import create_app,db
from selenium import webdriver

class SeleniumTestCase(unittest.TestCase):
    client=None
    @classmethod
    def setUpClass(cls):
        #启动firefox
        try:
            cls.client=webdriver.Firefox()
        except:
            pass
        if cls.client:
            cls.app=create_app('testing')
            cls.app_context=cls.app.app_context()
            cls.app_context.push()
            db.create_all()
            threading.Thread(target=cls.app.run).start()
    @classmethod
    def tearDownClass(cls):
        if cls.client:
            cls.client.get('http://localhost:5000/shutdown')
            cls.client.close()
            db.drop_all()
            db.session.remove()
            cls.app_context.pop()

    def setUp(self):
        if not self.client:
            self.skipTest('Firefox is invailable')
    
    def tearDown(self):
        pass
    
    def test_home_page(self):
        self.client.get('http://localhost:5000/')
        self.assertTrue(re.search('Home',self.client.page_source))
    
    
