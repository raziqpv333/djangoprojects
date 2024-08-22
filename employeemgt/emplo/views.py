from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
# Create your views here.
def emplo (req):
    return render(req,"emplo1.html")

def addemployee(req):
    if req.method=='POST':
        name=req.POST['name']
        age=int(req.POST['age'])
        salary=int(req.POST['salary'])
        jod=req.POST['job']
        data=employee.objects.create(name=name,age=age,jod=jod,salary=salary)
        data.save()
        return render (req,"addemplo.html")
    else:
        return render(req,'addemplo.html')
def display (req):
    data1=employee.objects.all()
    return render (req,"emplo1.html",{"data11":data1})

def edit (req,id):
    a=employee.objects.get(pk=id)
    if req.method=='POST':
        name=req.POST['name']
        age=int(req.POST['age'])
        salary=int(req.POST['salary'])
        jod=req.POST['job']
        employee.objects.filter (pk=id).update(name=name,age=age,jod=jod,salary=salary)
        return redirect(display)



    return render (req,"editemplo.html",{'data':a})

def delete(red,id):
    a=employee.objects.get(pk=id)
    a.delete()
    return redirect(display)
