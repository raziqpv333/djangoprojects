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

def html1(req):
    return render(req,'index.html')

def html2(req):
    a="HELLO"
    p="you okay"
    s=[10,20,30]
    student=[{"name":"arun","age":24,},{"name":"unni","age":22},{"name":"sinu","age":23},{"name":"josep","age":19},{"name":"kannan","age":20}]
    return render(req,'inox.html',{'data':a,'roll':p,'num':s,'student':student})

def form(req):
    if req.method=='POST':
        name=req.POST['name']
        age=int(req.POST['age'])
        return render(req,'form.html',{'data1':name,'data2':age})
    else :
       return render(req,'form.html')
std=[]
def todos(req):

     if req.method=='POST':
        name=req.POST['name']
        age=int(req.POST['age'])
        id=int(req.POST['id'])
        mark=int(req.POST['mark'])
        std.append({'id':id,'name':name,'age':age,'mark':mark})
        return render(req,"todos.html",{'data11':std})
     else:
        return render(req,'todos.html')         