from typing import ItemsView
from django.core.checks import messages
from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render,HttpResponse 
from home.models import Task , Contact 
from datetime import datetime
from django.contrib import messages
# Create your views here.
def home(request):
    context={'success':False}
    if request.method =="POST":
        #handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        counts = request.POST['counts']
        # print(title,desc)
        ins = Task(taskTitle=title, taskDesc=desc , counts = counts)
        ins.save()
        context={'success':True}
    return render(request, 'index.html',context)
    #can pass dictationary to render


    

def tasks(request):
    allTasks = Task.objects.all()     #will fetch all the tasks from my task models
    context = {'tasks':allTasks}
    #print(allTasksS)
    # for item in allTasks:
    #     print(item.taskTitle/taskDesc)
    return render(request, 'tasks.html',context)

def contact(request):
   
    if request.method == 'POST':    
        name= request.POST.get('name')    
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        description= request.POST.get('description')
        contact=Contact(name=name , email = email , phone= phone , description= description , date = datetime.today())
        contact.save()
        messages.success(request, 'Your Messege Had been Sent !')
    
        
    return render(request,'contact.html' )




def delete_task(request, aditya):
    task = Task.objects.get(id=aditya)
    task.delete()
    return redirect("tasks")
    
def about(request) :
    return render(request, 'about.html')


def aditya(request) :
    return render(request, 'aditya.html')

def sadid(request) :
    return render(request, 'sadid.html')

def vais(request) :
    return render(request, 'vais.html')

def adnan(request) :
    return render(request, 'adnan.html')
    
    
    

    

