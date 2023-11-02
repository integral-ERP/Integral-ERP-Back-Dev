from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from wareHouse.models import  PickUpOrder, ReceptionOrder, ReleaseOrder
from wareHouse.api.serializers import PickUpOrderSerializer, ReceptionOrderSerializer, ReleaseOrderSerializer
from rest_framework import status
from rest_framework.response import Response

class PickUpOrderApiViewSet(ModelViewSet):
    serializer_class = PickUpOrderSerializer
    queryset = PickUpOrder.objects.all().select_related('employee')
    filter_backends = [filters.SearchFilter]
    search_fields = ['status','number','creation_date','pick_up_date','delivery_date','date','issued_by','destination_agent','employee','shipper','pick_up_location','consignee','delivery_location','inland_carrier','main_carrier','pro_number','tracking_number','supplier','invoice_number','purchase_order_number']

class ReceptionOrderApiViewSet(ModelViewSet):
    serializer_class = ReceptionOrderSerializer
    queryset = ReceptionOrder.objects.all().select_related('employee')
    filter_backends = [filters.SearchFilter]
    search_fields = ['status','number','creation_date','employee','issued_by','destination_agent','shipper','consignee','client_to_bill','main_carrier','commodities','events','attachments']

class ReleaseOrderApiViewSet(ModelViewSet):
    serializer_class = ReleaseOrderSerializer
    queryset = ReleaseOrder.objects.filter(disabled=False).select_related('employee')
    filter_backends = [filters.SearchFilter]
    search_fields = ['status', 'number', 'creation_date', 'employee', 'issued_by', 'client_to_bill', 'carrier', 'commodities']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True  # Mark the record as disabled
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)