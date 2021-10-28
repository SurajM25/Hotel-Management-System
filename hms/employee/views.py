from django.shortcuts import redirect, render
from .models import Room,Customer,Services,Uses,CustomerLog,Bill
from django.db.models import Count
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.http import HttpResponse
from head.models import Employee
from hotel.models import onlinebooking
from django.contrib.auth.models import auth
from django.contrib import messages
from head.utils import render_to_pdf
from django.http import HttpResponse
from django.views.generic import View


class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return ''

def register(request):
    if request.method == 'POST' and 'num'  in request.POST :
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        emailid = request.POST['emailid']
        address = request.POST['address']
        phoneno = request.POST['phoneno']
        children = request.POST['children']
        adults = request.POST['adults']
        roomtype = request.POST['roomtype']
        aadharno = request.POST['aadharno']
        daysstayed = request.POST['daysstayed']
        sex = request.POST['sex']
        num = request.POST['num']
        
        rooms = Room.objects.all()
        #Employee.objects.filter(emailid=emailid).exists()

        # for i in Room.objects.all():
        #     if i.roomtype=="Standard":
        #         i.price=1000
        #     elif i.roomtype=='Delux':
        #         i.price =2000
        #     else:
        #         i.price=3500
        #     i.save()

        for i in Room.objects.filter(roomno=num):
            if i.vacancy==True:
                roomno=i.id
                customer = Customer(firstname=firstname,lastname=lastname,age=age,emailid=emailid,address=address,phoneno=phoneno,children=children,
                adults=adults,roomtype=roomtype,aadharno=aadharno,daysstayed=daysstayed,sex=sex,room_id=i)
                customer.save()
                # customer = Customer.objects.raw('''INSERT INTO Customer (firstname, lastname, age, emailild, address, children, adults, roomtype, aadharno, daysstayed,room_id) 
                # VALUES (firstname,lastname,age,sex,phoneno,emailid,address,chindren,adults,roomtype,aadharno,daysstayed,sex,i)''');
                # customer.save()
                customerlog = CustomerLog(firstname=firstname,lastname=lastname,age=age,emailid=emailid,address=address,phoneno=phoneno,children=children,
                adults=adults,roomtype=roomtype,aadharno=aadharno,daysstayed=daysstayed,sex=sex,room_id=i)
                customerlog.save()
                
        
                roomno=Room.objects.get(id=roomno)
                i.occupied_by=customer
                i.vacancy = False
                i.save()
                break
        

        
    #     print('aaaa')
        return redirect('vacant-rooms')

    else:
        num = request.POST['number']
        room = Room.objects.filter(roomno=num).first()
        roomtype = room.roomtype
        print(roomtype)
        return render(request,'employee/register-cust.html',{'num':num,'roomtype':roomtype})

def view_rooms(request):
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        emailid = request.POST['emailid']
        address = request.POST['address']
        phoneno = request.POST['phoneno']
        children = request.POST['children']
        adults = request.POST['adults']
        roomtype = request.POST['roomtype']
        aadharno = request.POST['aadharno']
        daysstayed = request.POST['daysstayed']
        sex = request.POST['sex']
        
        rooms = Room.objects.all()

        customer = Customer(firstname=firstname,lastname=lastname,age=age,emailid=emailid,address=address,phoneno=phoneno,children=children,
        adults=adults,roomtype=roomtype,aadharno=aadharno,daysstayed=daysstayed,sex=sex)
        customer.save()
    else:
        rooms = Room.objects.all()
        return render(request,'employee/view-rooms.html',{'rooms':rooms})  #to view vacant rooms
    
def view_not_rooms(request):
        rooms = Room.objects.all()
        return render(request,'employee/view-not-vacant.html',{'rooms':rooms}) #to view booked rooms

def view_customer(request):
    if request.method == 'POST':
        num = request.POST['number']
        i= Room.objects.filter(roomno=num).first()
        customer = Customer.objects.filter(room_id=i).first()
        #uses = Uses.objects.filter(customer_id=customer)
       # Services.objects.filter(id=[uses.id])   
        #services = Services.objects.filter(uses__id=uses)
        
        services = Services.objects.filter(uses__customer=customer).distinct()
        #count = Uses.objects.filter(customer_id=customer).Count('customer_id','service_id')
        counts = Services.objects.filter(uses__customer=customer).annotate(times_used=Count('uses'))
        inc = Counter
        return render(request,'employee/asdd.html',{'customer':customer,'i':i,'services':services,'counts':counts,'inc':inc}) #,{'customer':customer}
    else:
     return render(request,'employee/cust-info.html')

def services(request):
    customer = Customer.objects.all()

    return render(request,'employee/servives.html',{'customer':customer})

def add_services(request):
    if request.method == "POST" and 'services' in request.POST:
        services = request.POST["services"]
        room = request.POST["room"]
        room_id = Room.objects.filter(id=room).first()
        customer = Customer.objects.filter(room_id=room_id).first()
        service = Services.objects.filter(id=services).first()
        uses = Uses.objects.create(customer=customer,service_id=service)
        uses.save()
        return redirect('non-vacant-rooms')
    else:
        room = request.POST['room']
        room = Room.objects.filter(id=room).first()
        services = Services.objects.all()
        print('alsk')
        return render(request,'employee/add-seervices.html',{'services':services,'room':room})

class GeneratePDF(View):
    def post(self, request, *args, **kwargs):
        cust = request.POST['cust']
        customer = Customer.objects.filter(id=cust).first()
        customerlog = CustomerLog.objects.filter(id=customer.id).first()
        services = Services.objects.filter(uses__customer=customer)
        room = Room.objects.filter(occupied_by=customer).first()
        uses = Uses.objects.filter(customer=customer)
        amt=0
        i=0
        for j in services:
            amt=amt+j.price
        
        template = get_template('head/invoice.html')
        context = {
            "customer": customer,
            "services": services,
            "billno" : i,
            "room" : room,
            'amount' :room.price*customer.daysstayed,
            "uses" :uses,
            "amt" :amt,
            'tamt':amt+room.price*customer.daysstayed,
            'ttamt': (amt+amt*0.13 + room.price*customer.daysstayed +room.price*customer.daysstayed*0.12) +  (amt+amt*0.13 + room.price*customer.daysstayed +room.price*customer.daysstayed*0.12)*0.18

            
           
        }
        print(amt)
        ttamt=amt+amt*0.13 + room.price*customer.daysstayed +room.price*customer.daysstayed*0.12 +  (amt+amt*0.13 + room.price*customer.daysstayed +room.price*customer.daysstayed*0.12)*0.18
        print(customerlog)
        bill = Bill(amount=ttamt,customer_id=customer.id)
        bill.save()
        i=i+1
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

def checkout(request):
    if request.method=='POST':
        cust = request.POST['cust']
        customer = Customer.objects.filter(id=cust).first()
        r = Room.objects.filter(occupied_by=customer).first()
        r.vacancy = True
        r.save()
        customer.delete()
        return redirect("non-vacant-rooms")
    return redirect("non-vacant-rooms")

def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']

        employee = auth.authenticate(firstname=username,password=password)
        print(employee)

        # if employee is not None:
        #     auth.login(request,employee)
        #     return render(request,'register/html')
        if Employee.objects.filter(firstname=username).exists():
            if Employee.objects.filter(password=password):
                messages.success(request,'Loged Out')
                return redirect('vacant-rooms')
            else:
                messages.error(request,'Wrong emailid')
                return redirect('login')
        else:
            messages.error(request,'wrong password or username')
            return redirect('login')
                
        # else:
        #     messages.error(request,'Email id dosent exist')
        #     return redirect('login')
            
    else:
        return render(request,'employee/login.html')        


def update(request):
    customer = Customer.objects.all()
    return render(request,'employee/update.html',{'customer':customer})

def update_1(request):
    if request.method == "POST" and 'firstname' not in request.POST:
        customer = request.POST['customer']
        print(customer)
        customer = Customer.objects.filter(id=customer).first()
        return render(request,'employee/update_1.html',{'customer':customer})

    if request.method == 'POST' and 'firstname'  in request.POST :
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        emailid = request.POST['emailid']
        address = request.POST['address']
        phoneno = request.POST['phoneno']
        children = request.POST['children']
        adults = request.POST['adults']
        aadharno = request.POST['aadharno']
        daysstayed = request.POST['daysstayed']
        sex = request.POST['sex']
      

        customer = Customer.objects.filter(firstname=firstname).first()
        customer.firstname= firstname
        customer.lastname= lastname
        customer.age = age
        customer.emailid = emailid
        customer.address = address
        customer.phoneno = phoneno
        customer.children = children
        customer.adults = adults
        customer.aadharno = aadharno
        customer.daysstayed = daysstayed
        customer.sex = sex
        customer.save()

        customerlog = CustomerLog.objects.filter(firstname=firstname).first()
        customerlog.firstname= firstname
        customerlog.lastname= lastname
        customerlog.age = age
        customerlog.emailid = emailid
        customerlog.address = address
        customerlog.phoneno = phoneno
        customerlog.children = children
        customerlog.adults = adults
        customerlog.aadharno = aadharno
        customerlog.daysstayed = daysstayed
        customerlog.sex = sex
        customerlog.save()
        return redirect('vacant-rooms')
 
def online(request):
    online = onlinebooking.objects.all()
    return render(request,'employee/online.html',{'online':online})
    

