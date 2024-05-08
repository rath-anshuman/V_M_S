from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

def generate_vendor_code():
    now = datetime.now()
    return 'ven{0:%Y%m%d%H%M%S}'.format(now)


class Vendors(models.Model):
    vender_id=models.AutoField(unique=True,primary_key=True)
    name = models.CharField(max_length=50)
    contact_details = models.TextField(max_length=400)
    address = models.TextField(max_length=600)
    vendor_code = models.CharField(max_length=20,default=generate_vendor_code,unique=True,editable=False)

    def __str__(self):
        return (f"{self.name}-{self.vender_id}")
    

class PerformanceMetrics(models.Model):
    vendor = models.ForeignKey('Vendors', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])

