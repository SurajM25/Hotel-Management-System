from django.urls import path, include
from . import views
urlpatterns = [
    path('register/', views.register,name='customer'),
    path('rooms/',views.view_rooms,name='vacant-rooms'),
    path('rooms_1/',views.view_not_rooms,name='non-vacant-rooms'),
    path('view_customer/',views.view_customer,name='view-customer'),
    path('services/',views.services,name='services'),
    path('services_add/',views.add_services,name='add-services'),
    path('customer_printbill/',views.GeneratePDF.as_view(),name='emp-checkout'),
    path('',views.login,name='login'),
    path('checkout/',views.checkout,name='checkout'),
    path('update/',views.update,name='update'),
    path('update_1/',views.update_1,name='update_1'),
    path('view_onlinebooking/',views.online,name='online'),
]