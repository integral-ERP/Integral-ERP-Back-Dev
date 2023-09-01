from rest_framework import serializers
from wareHouse.models import shipper, issuedBy, pickUpLocation, consignee, deliveryLocation, pickUpOrder, pieces

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
                    'forwarAgent',
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
    class Meta:
        model = pickUpOrder
        fields = ['id',
                    'status',
                    'number',
                    'creationDate',
                    'pickUpDate',
                    'deliveryDate',
                    'date',
                    'issuedByKey',
                    'destinationAgentKey',
                    'employeekey',
                    'shipperkey',
                    'PickUpLocationkey',
                    'consigneekey',
                    'deliveryLocationkey',
                    'inlandCarrierKey',
                    'mainCarrierKey',
                    'proNumber',
                    'trackingNumber',
                    'supplierKey',
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