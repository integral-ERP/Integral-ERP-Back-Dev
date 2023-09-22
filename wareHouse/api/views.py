from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from wareHouse.models import  pickUpOrder, pieces
from wareHouse.api.serializers import    piecesSerializer,  pickUpOrderSerializer

class pickUpOrderApiViewSet(ModelViewSet):
    serializer_class = pickUpOrderSerializer
    queryset = pickUpOrder.objects.all().select_related('destinationAgentKey', 'employeekey', 'inlandCarrierKey', 'mainCarrierKey', 'supplierKey')
    filter_backends = [filters.SearchFilter]
    search_fields = ['id',
                    'status',
                    'number',
                    'creationDate',
                    'pickUpDate',
                    'deliveryDate',
                    'date',
                    'issuedByKey',
                    'destinationAgentKey',
                    'destinationAgent',
                    'employeekey',
                    'employee',
                    'shipperkey',
                    'PickUpLocationkey',
                    'consigneekey',
                    'deliveryLocationkey',
                    'inlandCarrierKey',
                    'inlandCarrier',
                    'mainCarrierKey',
                    'mainCarrier',
                    'proNumber',
                    'trackingNumber',
                    'supplierKey',
                    'supplier',
                    'invoiceNumber',
                    'purchaseOrderNum']

class piecesApiViewSet(ModelViewSet):
    serializer_class = piecesSerializer
    queryset = pieces.objects.all()

