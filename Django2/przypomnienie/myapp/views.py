from typing import Any
from urllib import response
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home_page(self):
    html = '<h1>Hello world</h1>'
    return HttpResponse(html)

def post_form(self):
    return HttpResponse()