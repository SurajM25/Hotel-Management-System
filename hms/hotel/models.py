from django.db import models

# Create your models here.
class onlinebooking(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    room_type = models.CharField(max_length=10)
    booking_date = models.DateField()
    
