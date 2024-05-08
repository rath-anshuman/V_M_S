from .models import Vendors,PerformanceMetrics
from Purchase_Orders.models import PurchaseOrder 
from Purchase_Orders.serialization import PurchaseOrderSerializer 
from .serialization import VendorsSerializer,PerformanceMetricsSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from django.db.models import Sum,Avg,F,ExpressionWrapper,DurationField
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class VendorsViewSet(viewsets.ModelViewSet):
    queryset=Vendors.objects.all()
    serializer_class=VendorsSerializer
    permission_classes = [IsAuthenticated]



@api_view(['GET'])
def vendor_performance(request, vendor_id):

    vendor = get_object_or_404(Vendors, pk=vendor_id)

    # completed purchase orders
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    total_completed_pos = completed_pos.count()


    # on_time_delivery_rate
    on_time_pos = completed_pos.filter(delivery_date__lte=F('delivery_date'))
    total_completed_pos_ontime = on_time_pos.count()
    on_time_delivery_rate = (total_completed_pos / total_completed_pos_ontime) * 100 if total_completed_pos != 0 else 0
    on_time_delivery_rate = format(on_time_delivery_rate, ".2f")
    on_time_delivery_rate = (f"{on_time_delivery_rate}%")


    # quality rating average
    average_rating = completed_pos.aggregate(Avg('quality_rating')) ['quality_rating__avg']
    quality_average_rating = format(average_rating, ".2f") if average_rating is not None else None
    quality_rating_avg = (f"{quality_average_rating}%")


    # average response time
    completed_pos_with_acknowledgment = PurchaseOrder.objects.filter(vendor=vendor,acknowledgment_date__isnull=False)

    annotated_pos = completed_pos_with_acknowledgment.annotate(response_time=ExpressionWrapper(F('acknowledgment_date') - F('issue_date'),output_field=DurationField()))
    
    avg_response_time = annotated_pos.aggregate(avg_response_time=Avg('response_time'))['avg_response_time'] or 0
    
    avg_response_time = avg_response_time.total_seconds()  
    avg_response_time = f"{avg_response_time / 3600:.2f} hours"

    
    # fulfilment rate
    fulfilled_pos_count = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
    fulfillment_rate = (fulfilled_pos_count / total_completed_pos) * 100 if total_completed_pos != 0 else 0
    
    # # Create or update PerformanceMetrics instance
    performance_metrics = PerformanceMetrics.objects.get_or_create(vendor=vendor)
    performance_metrics.on_time_delivery_rate = on_time_delivery_rate
    performance_metrics.quality_rating_avg = quality_rating_avg
    performance_metrics.average_response_time = avg_response_time
    performance_metrics.fulfillment_rate = fulfillment_rate
    performance_metrics.save()
    
    # Return the calculated performance metrics
    return Response({
        'on_time_delivery_rate': on_time_delivery_rate,
        'quality_rating_avg': quality_rating_avg,
        'average_response_time': avg_response_time,
        'fulfillment_rate': fulfillment_rate
    })