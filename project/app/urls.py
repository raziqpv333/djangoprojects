from django.urls import path
from . import views
urlpatterns=[
    path("func1",views.function1),
    path("func2",views.function2),
    path("func3/<a>",views.function3),
    path("func4/<int:b>",views.function4),
    path("func5/<c>",views.function5),
    path("html1",views.html1),
    path("html2",views.html2),
    path("form",views.form),
    path("todos1",views.todos),
    path("tabletodo2/<int:id>",views.tabletodo),
    path("delete/<int:id>",views.delete),
    path("userform",views.user_form),
    path('modelform',views.modform),
    path("base",views.base),
    path("addproduct",views.addproduct),
    path("displayproduct",views.displayproduct)
]
