from rest_framework import serializers

from maintenance.models import employee

from wareHouse.models import  pickUpOrder, pieces

from maintenance.api.serializers import employeeSerializer, forWardingAgentsSerializer, carrierSerializer, customerSerializer



class pickUpOrderSerializer(serializers.ModelSerializer):
    destinationAgent = forWardingAgentsSerializer(required=False, source="destinationAgentKey")
    employee         =   employeeSerializer(required=False, source="employeekey")
    inlandCarrier    =   carrierSerializer(required=False, source="inlandCarrierKey")    
    mainCarrier      =   carrierSerializer(required=False, source="mainCarrierKey")
    supplier         =   customerSerializer(required=False, source="supplierKey")

    class Meta:
        model = pickUpOrder
    
        fields = [  'id',
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
                    'purchaseOrderNum'
                ]  


class piecesSerializer(serializers.ModelSerializer):
    class Meta:
        model = pieces
        fields = [  'id',
                    'status',
                    'package',
                    'description',
                    'pieces',
                    'length',
                    'height',
                    'width',
                    'width',
                    'weight',
                    'volume'
                ]
        