from django.shortcuts import render

# Create your views here.

def employee_register(request):
    return render(request, 'employee/employee_register.html', {})