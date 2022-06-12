from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

brand = [
    ('dell', 'dell'),
    ('lenovo', 'lenovo'),
    ('acer', 'acer'),
    ('hp', 'hp')
]

# Create your models here.
class Laptop(models.Model):
    laptop_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    model =models.CharField(max_length=50)
    brand = models.CharField(max_length=50, choices=brand)
    ram = models.CharField(max_length=50)
    price = models.FloatField()
    date = models.DateField()
    phoneNumber = PhoneNumberField()
    seller = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
