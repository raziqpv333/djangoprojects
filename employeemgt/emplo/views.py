from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib.auth.models import auth


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
def login(req):
    if req.method=='POST':
        name=req.POST['username']
        password=req.POST['password']
        data=auth.authenticate(username=name,password=password)
        if data is not None:
            auth.login(req,data)
            return redirect(home)
    return render(req,'login.html')
    
def home(req):
    return render(req,'home.html')


def logout(req):
    auth.logout(req)
    return redirect(login)

def productadd(req):
    if req.method=='POST':
        name=req.POST['name']
        price=int(req.POST['price'])
        dis=req.POST['discription']
        img=req.FILES['image']
        data=product.objects.create(name=name,price=price,dis=dis,img=img)
        data.save()
    return render(req,'productadded.html')    


def productdisplay(req):
    a=product.objects.all()
    return render(req,"productdisplay.html",{'a':a})

