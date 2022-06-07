from pydoc import resolve
from urllib import response
from django.test import TestCase
from django.urls import resolve
from myapp.views import home_page
from selenium.webdriver.common.keys import Keys
import time

class HomePageTest(TestCase): 

    def test_url(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_view(self): 
        page = self.client.get('/', follow= True)
        self.assertEqual(page.content.decode('utf8'), '<h1>Hello world</h1>')
        self.assertEqual(page.status_code, 200)
    
