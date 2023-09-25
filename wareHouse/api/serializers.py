from rest_framework import serializers

from wareHouse.models import  PickUpOrder, pieces
from maintenance.api.serializers import AgentSerializer,CustomerSerializer,EmployeeSerializer,CarrierSerializer, ShipperSerializer,PickUpLocationSerializer,ConsigneeSerializer,DeliveryLocationSerializer



class PickUpOrderSerializer(serializers.ModelSerializer):
    issued_byObj = AgentSerializer(required=False,source='issued_by')
    destination_agentObj = AgentSerializer(required=False,source='destination_agent')
    employeeObj = EmployeeSerializer(required=False,source='employee')
    shipperObj = ShipperSerializer(required=False,source='shipper')
    pickUpLocationObj = PickUpLocationSerializer(required=False,source='pick_up_location')
    consigneeObj = ConsigneeSerializer(required=False,source='consignee')
    deliveryLocationObj = DeliveryLocationSerializer(required=False,source='delivery_location')
    inland_carrierObj = CarrierSerializer(required=False,source='in_land_carrier')
    main_carrierObj = CarrierSerializer(required=False,source='main_carrier')
    supplierObj = CustomerSerializer(required=False,source='supplier')
    
    class Meta:
        model = PickUpOrder
       
        fields = [  'status','number','creation_date','pick_up_date','delivery_date','date','issued_by','issued_byObj','destination_agent','destination_agentObj','employee','employeeObj','shipper','shipperObj','pick_up_location','pickUpLocationObj','consignee','consigneeObj','delivery_location','deliveryLocationObj','inland_carrier','inland_carrierObj','main_carrier','main_carrierObj','pro_number','tracking_number','supplier','supplierObj','invoice_number','purchase_order_number'
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
        