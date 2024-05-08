# Generated by Django 4.2.11 on 2024-05-07 15:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_details', models.TextField(max_length=400)),
                ('address', models.TextField(max_length=600)),
                ('on_time_delivery_rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('quality_rating_avg', models.FloatField(choices=[(1.0, '1 - Poor'), (2.0, '2 - Fair'), (3.0, '3 - Good'), (4.0, '4 - Very Good'), (5.0, '5 - Excellent')], validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
                ('average_response_time', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('fulfillment_rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]
