from django.urls import path
from . import views

urlpatterns=[
     path("emplo",views.emplo),
     path("add",views.addemployee),
     path("dis",views.display)
]