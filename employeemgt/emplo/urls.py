from django.urls import path
from . import views

urlpatterns=[
     path("emplo",views.emplo),
     path("add",views.addemployee),
     path("dis",views.display),
     path("edit/<id>",views.edit),
     path("delete/<id>",views.delete),
     path("login",views.login),
     path("home",views.home),
     path("logout",views.logout)
]