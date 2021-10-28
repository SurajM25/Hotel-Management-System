
from django.shortcuts import render,redirect
from .models import Employee
from django.contrib.auth.admin import messages
from employee.models import Services,Room,CustomerLog,Customer
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from employee.models import Bill,CustomerLog,Customer 
from django.db.models import Sum
from django.contrib import auth
from django.contrib.auth.models import User
# Create your view here



def home(request):
    bill= list(Bill.objects.aggregate(Sum('amount')).values())[0]
    customer = Customer.objects.all().count()
    customerlog = CustomerLog.objects.all().count()
    employee = Employee.objects.all().count()
    return render(request,'head/head-home.html',{'bill':bill,'customer':customer,'customerlog':customerlog,'employee':employee})

def view_employee(request):
    employee = Employee.objects.all()
    return render(request,'head/view-employee.html',{'employee':employee})

def view_services(request):
    services=Services.objects.all()
    return render(request,'head/view-services.html',{'services':services})

def view_rooms(request):
    rooms = Room.objects.all()
    return render(request,'head/view-rooms.html',{'rooms':rooms})

def view_customer(request):
    customerlog = CustomerLog.objects.all()
    return render(request,'head/view-cust.html')

def register(request):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        emailid = request.POST['emailid']
        address = request.POST['address']
        phoneno = request.POST['phoneno']
        designation = request.POST['designation']
        password = request.POST['password']
        password1 = request.POST['password1']
        salary = request.POST['salary']
        sex = request.POST['sex']
        aadharno = request.POST['aadharno']

        
        if password == password1:
            if Employee.objects.filter(emailid=emailid).exists():
                messages.error(request,f'Employee exists')
                return redirect('employee-register')
            else:
                employee = Employee(firstname=firstname,lastname=lastname,age=age,emailid=emailid,address=address,phoneno=phoneno,
                                     designation=designation,password=password,aadharno=aadharno,salary=salary,sex=sex)
                employee.save()
                messages.success(request,f'Employee created')
                return redirect('/')
        else:
            messages.error(request,f'Password Missmatch')
            return redirect('employeee-register')
    else:
        return render(request,'head/emp-reg.html')

def reg_services(request):
    if request.method == 'POST':
        servicename = request.POST['servicename']
        price = request.POST['price']
        service = Services.objects.create(service_name = servicename, price = price)
        service.save()
        return redirect('/')
    else:
        return render(request,'head/services-reg.html')

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'POST:':
            cust = request.POST['cust']
            customer = Customer.objects.filter(id=cust)
            template = get_template('head/invoice.html')
            context = {
                "customer":customer
            }
            html = template.render(context)
            pdf = render_to_pdf('head/invoice.html', context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Invoice_%s.pdf" %("12341231")
                content = "inline; filename='%s'" %(filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename='%s'" %(filename)
                response['Content-Disposition'] = content
                return response
        return HttpResponse("Not found")

def update_1(request):
    if request.method == "POST" and 'firstname' not in request.POST:
        customer = request.POST['customer']
        print(customer)
        customer = Employee.objects.filter(id=customer).first()
        return render(request,'head/employee_update.html',{'customer':customer})
    
    if request.method == 'POST' and 'firstname'  in request.POST :
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        emailid = request.POST['emailid']
        address = request.POST['address']
        phoneno = request.POST['phoneno']
        pas = request.POST['pas']
        adults = request.POST['adults']
        aadharno = request.POST['aadharno']
        daysstayed = request.POST['daysstayed']
        sex = request.POST['sex']
      

        customer = Employee.objects.filter(firstname=firstname).first()
        customer.firstname= firstname
        customer.lastname= lastname
        customer.age = age
        customer.emailid = emailid
        customer.address = address
        customer.phoneno = phoneno
        customer.salary = adults
        customer.designation = daysstayed
        customer.aadharno = aadharno
        customer.password = pas
        customer.sex = sex
        customer.save()
        bill= list(Bill.objects.aggregate(Sum('amount')).values())[0]
        customer = Customer.objects.all().count()
        customerlog = CustomerLog.objects.all().count()
        employee = Employee.objects.all().count()
        return render(request,'head/head-home.html',{'bill':bill,'customer':customer,'customerlog':customerlog,'employee':employee})

def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']

        employee = auth.authenticate(username=username,password=password)
        print(employee)

        if employee is not None:
            auth.login(request,employee)
            return redirect('homee')
        # if User.objects.filter(username=username).exists():
        #     if Employee.objects.filter(password=password):
        #         messages.success(request,'Loged Out')
        #         return redirect('vacant-rooms')
        #     else:
        #         messages.error(request,'Wrong emailid')
        #         return redirect('login')
        else:
            messages.error(request,'wrong password or username')
            return render(request,'head/login.html')
                
        # else:
        #     messages.error(request,'Email id dosent exist')
        #     return redirect('login')
            
    else:
        return render(request,'head/login.html')        