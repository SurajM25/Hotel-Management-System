from django.shortcuts import render,redirect
from . import models
from employee.models import Services
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'hotel/index.html')

def onlinebooking(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['email']
        phone_number = request.POST['phone_no']
        room_type = request.POST['room_type']
        booking_date = request.POST['booking_date']
        print(booking_date)
        online = models.onlinebooking(name=name,email=email,phone_number=phone_number,room_type=room_type,booking_date=booking_date)
        online.save()
        
        message = 'Your reservation has been recieved. Visit Delights on the day of reservation to ensure confirmation of your reservation'
        send_mail('Booking Recived',message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
        messages.success(request,'Booking has been confirmed. Check your email for additionsl details.')
        return redirect('onlinebooking')
    else:
        return render(request,'hotel/onlinebooking.html')

def services(request):
    services = Services.objects.all()
    return render(request,'hotel/services.html',{'services':services})

