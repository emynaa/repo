import imp
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vm, name='vm'),
    path('myform', views.myform, name='myform'),
    path('index', views.function , name='index')
]