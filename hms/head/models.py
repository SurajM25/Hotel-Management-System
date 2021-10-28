from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from datetime import datetime    
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.
def create_employee(sender,instance,**kwargs):
        aa=Employee.objects.create(firstname=instance.username,password=instance.password,datejoined=instance.date_joined,designation="Head",salary=100000)
        aa.save()

class Employee(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=10,null=True)
    phoneno = models.IntegerField(null=True)
    emailid = models.CharField(max_length=25,null=True)
    address = models.CharField(max_length=50)
    salary = models.IntegerField()
    designation = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    aadharno = models.CharField(max_length=15,null=True)
    datejoined = models.DateField(default=datetime.now)

    def __str__(self):
        if self.firstname=='None':
            return ''
        else:
             return str(self.firstname+' '+self.lastname)
    
    

post_save.connect(receiver=create_employee, sender=User)
