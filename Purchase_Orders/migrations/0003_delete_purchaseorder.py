# Generated by Django 4.2.11 on 2024-05-08 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase_Orders', '0002_alter_purchaseorder_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PurchaseOrder',
        ),
    ]
