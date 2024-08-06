from django.urls import path
from . import views
urlpatterns=[
    path("func1",views.function1),
    path("func2",views.function2),
    path("func3/<a>",views.function3),
    path("func4/<int:b>",views.function4),
    path("func5/<c>",views.function5)
]
