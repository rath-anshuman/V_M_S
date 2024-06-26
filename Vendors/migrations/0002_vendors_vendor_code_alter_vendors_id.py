# Generated by Django 4.2.11 on 2024-05-07 15:23

import Vendors.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendors',
            name='vendor_code',
            field=models.CharField(default=Vendors.models.generate_vendor_code, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='vendors',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
