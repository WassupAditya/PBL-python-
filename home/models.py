from django.db import models
#make migration - create changes and stores in a file 
# migrate - apply the pending changes created by makemigrations
# Create your models here.
class Contact(models.Model):
    name=models.CharField( max_length=122)
    email=models.CharField( max_length=122)
    phone=models.CharField( max_length=12)
    description=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name


class Task(models.Model):
    taskTitle = models.CharField(max_length=30)
    counts = models.CharField(max_length=30)
    taskDesc =models.TextField()
    time = models.DateTimeField(auto_now_add=True)
#below will show up the tasktitle as title of the task in the database !!!    
    def __str__(self):
        return self.taskTitle


