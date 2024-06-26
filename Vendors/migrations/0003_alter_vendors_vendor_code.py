# Generated by Django 4.2.11 on 2024-05-07 15:24

import Vendors.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendors', '0002_vendors_vendor_code_alter_vendors_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendors',
            name='vendor_code',
            field=models.CharField(default=Vendors.models.generate_vendor_code, editable=False, max_length=20, unique=True),
        ),
    ]
