from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from wareHouse.models import  PickUpOrder, ReceptionOrder, ReleaseOrder
from wareHouse.api.serializers import PickUpOrderSerializer, ReceptionOrderSerializer, ReleaseOrderSerializer
from rest_framework import status
from rest_framework.response import Response

class BaseModelViewSet(ModelViewSet):
    disabled_field = 'disabled'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        setattr(instance, self.disabled_field, True)
        instance.save()
        return Response(data = instance,status=status.HTTP_200_OK)

class PickUpOrderApiViewSet(BaseModelViewSet):
    serializer_class = PickUpOrderSerializer
    queryset = PickUpOrder.objects.filter(disabled=False).select_related('employee')
    filter_backends = [filters.SearchFilter]
    search_fields = ['status','number','creation_date','pick_up_date','delivery_date','date','issued_by','destination_agent','employee','shipper','pick_up_location','consignee','delivery_location','inland_carrier','main_carrier','pro_number','tracking_number','supplier','invoice_number','purchase_order_number']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReceptionOrderApiViewSet(BaseModelViewSet):
    serializer_class = ReceptionOrderSerializer
    queryset = ReceptionOrder.objects.filter(disabled=False).select_related('employee')
    filter_backends = [filters.SearchFilter]
    search_fields = ['status','number','creation_date','employee','issued_by','destination_agent','shipper','consignee','client_to_bill','main_carrier','commodities','events','attachments','weight']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReleaseOrderApiViewSet(BaseModelViewSet):
    serializer_class = ReleaseOrderSerializer
    queryset = ReleaseOrder.objects.filter(disabled=False).select_related('employee')
    filter_backends = [filters.SearchFilter]
    search_fields = ['status', 'number', 'creation_date', 'employee', 'issued_by', 'client_to_bill', 'carrier', 'commodities']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)