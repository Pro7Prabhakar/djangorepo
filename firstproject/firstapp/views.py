from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(req):
    s = '<h1>Hello Everyone!!!</h1>'
    return HttpResponse(s)
