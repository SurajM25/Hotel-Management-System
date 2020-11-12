from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
# Create your models here.
class Employee(models.Model):
    
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
    email_id=models.CharField(max_length=30)
    phone_no=models.IntegerField()
    age=models.IntegerField()
    aadhar_number=models.CharField(max_length=15)
    sex=models.CharField(max_length=5)
    address=models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)


