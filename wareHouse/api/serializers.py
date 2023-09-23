from rest_framework import serializers

from wareHouse.models import  PickUpOrder,Shipper, pieces
from maintenance.api.serializers import EmployeeSerializer



class PickUpOrderSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = PickUpOrder
        employeeObj = EmployeeSerializer(required=False,source='employee')
        fields = [  'status','number','creation_date','pick_up_date','delivery_date','date','issued_by','destination_agent','employee','employeeObj','shipper','pick_up_location','consignee','delivery_location','inland_carrier','main_carrier','pro_number','tracking_number','supplier','invoice_number','purchase_order_number'
                ] 
 

class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = [  'customer','agent','vendor'
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
        