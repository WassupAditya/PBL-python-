from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('tasks', views.tasks, name="tasks"),
    path("delete/<int:aditya>/", views.delete_task, name="delete_task"),
    path('contact', views.contact, name="contact"),
    path('about',views.about,name="about") , 
    path('aditya',views.aditya,name="aditya") ,
    path('sadid',views.sadid,name="sadid") ,
    path('vais',views.vais,name="vais") ,
    path('adnan',views.adnan,name="adnan") ,
]
