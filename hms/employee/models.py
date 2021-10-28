from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING, SET_NULL
from django.db.models.fields import NullBooleanField
from django.contrib import admin
from datetime import datetime    
from head.models import Employee


# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    phoneno = models.IntegerField()
    emailid = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    children = models.IntegerField()
    adults = models.IntegerField()
    roomtype = models.CharField(max_length=10)
    aadharno = models.CharField(max_length=15)
    daysstayed = models.IntegerField()
    date_visited = models.DateTimeField(default=datetime.now)
    emp_id = models.ForeignKey(Employee,on_delete=models.SET_NULL,blank=True,null=True)
    room_id=models.OneToOneField('employee.Room',on_delete=SET_NULL,null=True)

    def __str__(self):
        if self.firstname == None:
            return ''
        else:
            return str(self.id)

class CustomerLog(models.Model):
   firstname = models.CharField(max_length=15)
   lastname = models.CharField(max_length=15)
   age = models.IntegerField()
   sex = models.CharField(max_length=10)
   phoneno = models.IntegerField()
   emailid = models.CharField(max_length=25)
   address = models.CharField(max_length=50)
   children = models.IntegerField()
   adults = models.IntegerField()
   roomtype = models.CharField(max_length=10)
   aadharno = models.CharField(max_length=15)
   daysstayed = models.IntegerField()
   date_visited = models.DateTimeField(default=datetime.now)
   #emp_id = models.ForeignKey(Employee,on_delete=models.SET_NULL,blank=True,null=True)
   room_id=models.ForeignKey('employee.Room',on_delete=SET_NULL,null=True,unique=False)


class Room(models.Model):
    roomno = models.IntegerField()
    roomtype = models.CharField(max_length=10)
    vacancy = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    occupied_by = models.OneToOneField(Customer,on_delete=SET_NULL,null=True,blank=True)

    def __str__(self):
        if self.roomno == None:
            return ''
        else:
            return str(self.roomno)

class Services(models.Model):
    service_name = models.CharField(max_length=15)
    price = models.IntegerField()
    #used_by = models.ManyToManyField(Customer,null=True,default=0)

    def __str__(self):
        if self.service_name == None:
            return ''
        else:   
            return str(self.service_name)

    

# class artist(models.Model):
#     name = models.CharField(max_length=200)
# class movie(models.Model):
#     title = models.CharField(max_length=100)
#     artists = models.ManyToManyField(artist, related_name = 'actor', through='roles')
# class role(models.Model):
#     role_name = models.CharField(max_length=100)
#     artist = models.ForeignKey(artist, on_delete=models.CASCADE)
#     movie = models.ForeignKey(movie, on_delete=models.CASCADE)


class Uses(models.Model):
    customer = models.ForeignKey(Customer,on_delete=CASCADE)
    service_id = models.ForeignKey(Services,on_delete=CASCADE)
    time_used = models.TimeField(default=datetime.now)

    def __str__(self):
        if self.customer == None:
            return ''
        else:   
            return str(self.customer)

class Uses_inline(admin.TabularInline):
    model = Uses
    extra = 1

class CustomerAdmin(admin.ModelAdmin):
    inlines = (Uses_inline,)

class ServicesAdmin(admin.ModelAdmin):
    inlines = (Uses_inline,)


class Bill(models.Model):
    amount = models.IntegerField()
    customer = models.OneToOneField(Customer,on_delete=SET_NULL,default=None,null=True)
    biling_date = models.DateTimeField(default=datetime.now)
    #payment_method = models.CharField(max_length=15)