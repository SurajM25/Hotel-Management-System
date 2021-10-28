from django.contrib import admin
from . import models
# Register your models here.
#admin.site.register(models.Customer)
admin.site.register(models.Room)
#admin.site.register(models.Services)
admin.site.register(models.CustomerLog)
admin.site.register(models.Uses)
admin.site.register(models.Customer,models.CustomerAdmin)
admin.site.register(models.Services,models.ServicesAdmin)
admin.site.register(models.Bill)
