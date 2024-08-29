from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

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
        return render(req,'todos.html',{'data11':std})

def tabletodo(req,id):
    pos=0
    stud={}
    for i in std:
        if i["id"]==id:
            stud=i
            pos=std.index(i)
    if req.method=='POST':
        name=req.POST['name']
        age=int(req.POST['age'])
        mark=int(req.POST['mark'])
        std[pos]={'id':id,'name':name,'age':age,'mark':mark}
        return redirect (todos)

    return render (req,'todostable.html',{'data4':stud})


def delete(req,id):
    for i in std:
        if i["id"]==id:
            std.remove(i)
            return redirect(todos)

        
def addmark (req):
    a=Student.objects.all()
    return render(req,'addmark.html',{'a':a})        


def user_form(req):
    if req.method=='POST':
        data=employee_form(req.POST)
        if data.is_valid():
            name=data.cleaned_data['name']
            age=data.cleaned_data['age']
            position=data.cleaned_data['position']
            data=employee.objects.create(name=name,age=age,position=position)
            data.save()
            


    data=employee_form()
    return render(req,'userform.html',{'data':data})

def modform(req):
   if req.method=='POST':
       data=model_form(req.POST)
       if data.is_valid():
           data.save()
           return redirect(modform)
           
   else:
         data=model_form()
         return render(req,"modelform.html",{'data':data})
   
def base(req):
    return render(req,"extend.html")


