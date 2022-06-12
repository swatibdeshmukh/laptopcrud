from django import forms
from .models import Laptop

ram = [
    ('8gb', '8b'),
    ('12gb', '12gb'),
    ('16gb', '16gb')
]
seller = [
    ('lotus', 'Lotus'),
    ('relience', 'Relience'),
    ('city collection', 'City Collection'),
    ('trends', 'Trends')
]

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

        labels = {
            'laptop_id': 'LAPTOP ID',
            'name': 'NAME',
            'model': 'MODEL',
            'brand': 'BRAND',
            'ram': 'RAM',
            'price': 'PRICE',
            'date': 'MANUFACTURING DATE',
            'phoneNumber': 'PHONE NUMBER',
            'seller': 'SELLER',
            'address': 'ADDRESS'
        }

        widgets={
            'laptop_id':forms.NumberInput(attrs={'placeholder': 'Enter Laptop Id'}),
            'name':forms.TextInput(attrs={'placeholder':'Enter Laptop Name'}),
            'model':forms.TextInput(attrs={'placeholder':'Enter Model Name'}),
            'ram':forms.RadioSelect(choices=ram),
            'price':forms.NumberInput(attrs={'placeholder':'Enter Laptop Price'}),
            'date':forms.DateInput(attrs={'type':'date'}),
            'phoneNumber': forms.NumberInput(attrs={'placeholder':'Enter Phone Number'}),
            'seller':forms.CheckboxSelectMultiple(choices=seller),
            'address':forms.Textarea(attrs={'placeholder':'Enter Shop Address', 'rows':3})


        }