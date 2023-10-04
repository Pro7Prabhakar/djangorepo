from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(req):
    s = '<h1>Hello Students welcome to Mahesh sir Django Classes</h1>'
    return HttpResponse(s)