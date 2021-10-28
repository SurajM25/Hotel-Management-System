
from django.urls import path, include
from . import views
urlpatterns = [
    path('login/', views.login,name='head-home'),
    path('', views.home,name='homee'),
    path('employee_register', views.register,name='employee-register'),
    path('services_register', views.reg_services,name='services-add'),
    path('employee_view', views.view_employee,name='view-employee'),
    path('services_view', views.view_services,name='view-services'),
    path('rooms_view', views.view_rooms,name='view-services'),
    path('customer_view', views.view_customer,name='view-customer'),
    path('pdf',views.GeneratePDF.as_view(),name='pdf'),
    path('update_employee/',views.update_1,name='employee-update')
]