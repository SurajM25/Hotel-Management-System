from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('onlinebooking/', views.onlinebooking,name='onlinebooking'),
    path('services/',views.services,name='services')
]