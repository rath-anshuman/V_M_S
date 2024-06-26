from django.contrib import admin
from django.urls import path,include


from rest_framework.routers import DefaultRouter

from Vendors.views import VendorsViewSet
from Vendors.views import vendor_performance
from Purchase_Orders.views import PurchaseOrdersViewSet

venrouter=DefaultRouter()
venrouter.register('vendors',VendorsViewSet,basename='vendors')
venrouter.register('purchase_orders',PurchaseOrdersViewSet,basename='purchase_orders')

from .views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include(venrouter.urls)),
    path('api/vendors/<int:vendor_id>/performance', vendor_performance, name='vendor-performance'),
]
