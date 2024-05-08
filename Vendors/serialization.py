from .models import Vendors,PerformanceMetrics
from rest_framework import serializers

class VendorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendors
        fields='__all__'




class PerformanceMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PerformanceMetrics
        fields='__all__'
