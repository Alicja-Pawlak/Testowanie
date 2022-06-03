import html
from django.http import HttpResponse
from django.test import TestCase
from django.urls import resolve
from myapp.views import home_page

class HomePageTest(TestCase): 

    def test_view(self): 
        request = HttpResponse()
        html = home_page(request)
        self.assertTrue(html.startswith('<!DOCTYPE html>')) 
        self.assertIn('<title>To-Do lists</title>', html) 
        self.assertTrue(html.endswith('</html>'))