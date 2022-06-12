# Generated by Django 4.0.4 on 2022-04-17 05:16

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('laptop_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('brand', models.CharField(choices=[('dell', 'dell'), ('lenovo', 'lenovo'), ('acer', 'acer'), ('hp', 'hp')], max_length=50)),
                ('ram', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('date', models.DateField()),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('seller', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]