from  .models import PurchaseOrder
from django.utils import timezone
from .serialization import PurchaseOrderSerializer

from rest_framework import viewsets,status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view,action
from rest_framework.response import Response

class PurchaseOrdersViewSet(viewsets.ModelViewSet):
    queryset=PurchaseOrder.objects.all()
    serializer_class=PurchaseOrderSerializer
    filterset_fields = ['vendor']
    

    @action(detail=True, methods=['post'])
    def acknowledge(self, request, pk=None):
        purchase_order = self.get_object()
        purchase_order.acknowledgment_date = timezone.now()
        purchase_order.save()
        return Response({'message': 'Purchase order acknowledged successfully.'}, status=status.HTTP_200_OK)