from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def function1(req):
    return HttpResponse('welcome')

def function2(req):
    return HttpResponse("to all")

def function3(req,a):
    return HttpResponse("family"+a)
def function4(req,b):
    return HttpResponse(b)
def function5(req,c):
    return HttpResponse(c)    