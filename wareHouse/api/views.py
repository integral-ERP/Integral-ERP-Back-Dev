from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from wareHouse.models import shipper, issuedBy, pickUpLocation, consignee, deliveryLocation, pickUpOrder, pieces
from wareHouse.api.serializers import pickUpLocationSerializer, consigneeSerializer, deliveryLocationSerializer, piecesSerializer,  pickUpOrderSerializer, issuedBySerializer, shipperSerializer


class shipperApiViewSet(ModelViewSet):
    serializer_class = shipperSerializer
    queryset = shipper.objects.all()

class issuedByApiViewSet(ModelViewSet):
    serializer_class = issuedBySerializer
    queryset = issuedBy.objects.all()

class pickUpLocationApiViewSet(ModelViewSet):
    serializer_class = pickUpLocationSerializer
    queryset = pickUpLocation.objects.all()

class consigneeApiViewSet(ModelViewSet):
    serializer_class = consigneeSerializer
    queryset = consignee.objects.all()

class deliveryLocationApiViewSet(ModelViewSet):
    serializer_class = deliveryLocationSerializer
    queryset = deliveryLocation.objects.all().select_related("destinationAgentKey")

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

