from typing import Any
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):

    html = request.content.decode('utf8')
    return html