# Generated by Django 4.2.11 on 2024-05-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendors', '0003_alter_vendors_vendor_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendors',
            old_name='id',
            new_name='vender_id',
        ),
        migrations.AlterField(
            model_name='vendors',
            name='average_response_time',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='vendors',
            name='quality_rating_avg',
            field=models.FloatField(),
        ),
    ]
