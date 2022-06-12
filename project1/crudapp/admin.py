from django.contrib import admin
from crudapp.models import Laptop
# Register your models here.

class laptopAdmin(admin.ModelAdmin):
    list_display = ['laptop_id', 'name','model', 'brand', 'ram', 'price', 'date', 'phoneNumber', 'seller', 'address']

admin.site.register(Laptop, laptopAdmin)