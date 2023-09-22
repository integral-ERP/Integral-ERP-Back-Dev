from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from wareHouse.models import  PickUpOrder, pieces
from wareHouse.api.serializers import    piecesSerializer,  PickUpOrderSerializer

class PickUpOrderApiViewSet(ModelViewSet):
    serializer_class = PickUpOrderSerializer
    queryset = PickUpOrder.objects.all().select_related('destinationAgentKey', 'employeekey', 'inlandCarrierKey', 'mainCarrierKey', 'supplierKey')
    filter_backends = [filters.SearchFilter]
    search_fields = ['status','number','creation_date','pick_up_date','delivery_date','date','issued_by','destination_agent','employee','shipper','pick_up_location','consignee','delivery_location','inland_carrier','main_carrier','pro_number','tracking_number','supplier','invoice_number','purchase_order_number']

class piecesApiViewSet(ModelViewSet):
    serializer_class = piecesSerializer
    queryset = pieces.objects.all()

