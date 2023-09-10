from rest_framework import serializers

from maintenance.models import employee

from wareHouse.models import shipper, issuedBy, pickUpLocation, consignee, deliveryLocation, pickUpOrder, pieces

from maintenance.api.serializers import employeeSerializer, forWardingAgentsSerializer, carrierSerializer, customerSerializer

class shipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = shipper
        fields = [  'id',
                    'customerName',
                    'vendorName',
                    'agentName'
                ]
  
class issuedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = issuedBy
        fields = [  'id',
                    'forWardingAgents',
                    'wareHouseProvider'
                ]

class pickUpLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = pickUpLocation
        fields = [  'id',
                    'customerName',
                    'vendorName',
                    'agentName'
                ]

class consigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = consignee
        fields = [  'id',
                    'customerName',
                    'vendorName',
                    'agentName',
                    'carrierName'
                ]

class deliveryLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = deliveryLocation
        fields = [  'id',
                    'customerName',
                    'vendorName',
                    'agentName',
                    'carrierName'
                ]

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
        