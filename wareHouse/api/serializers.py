from rest_framework import serializers

from wareHouse.models import  PickUpOrder, ReceptionOrder
from maintenance.api.serializers import AgentSerializer,CustomerSerializer,EmployeeSerializer,CarrierSerializer, ShipperSerializer,PickUpLocationSerializer,ConsigneeSerializer,DeliveryLocationSerializer,ClientToBillSerializer



class PickUpOrderSerializer(serializers.ModelSerializer):
    issued_byObj = AgentSerializer(required=False,source='issued_by')
    destination_agentObj = AgentSerializer(required=False,source='destination_agent')
    employeeObj = EmployeeSerializer(required=False,source='employee')
    shipperObj = ShipperSerializer(required=False,source='shipper')
    pickUpLocationObj = PickUpLocationSerializer(required=False,source='pick_up_location')
    consigneeObj = ConsigneeSerializer(required=False,source='consignee')
    deliveryLocationObj = DeliveryLocationSerializer(required=False,source='delivery_location')
    inland_carrierObj = CarrierSerializer(required=False,source='inland_carrier')
    main_carrierObj = CarrierSerializer(required=False,source='main_carrier')
    supplierObj = CustomerSerializer(required=False,source='supplier')
    
    class Meta:
        model = PickUpOrder
       
        fields = [  'status','number','creation_date','pick_up_date','delivery_date','date','issued_by','issued_byObj','destination_agent','destination_agentObj','employee','employeeObj','shipper','shipperObj','pick_up_location','pickUpLocationObj','consignee','consigneeObj','delivery_location','deliveryLocationObj','inland_carrier','inland_carrierObj','main_carrier','main_carrierObj','pro_number','tracking_number','supplier','supplierObj','invoice_number','purchase_order_number'
                ] 
 

class ReceptionOrderSerializer(serializers.ModelSerializer):
    issued_byObj = AgentSerializer(required=False,source='issued_by')
    destination_agentObj = AgentSerializer(required=False,source='destination_agent')
    shipperObj = ShipperSerializer(required=False,source='shipper')
    consigneeObj = ConsigneeSerializer(required=False,source='consignee')
    clientBillObj = ClientToBillSerializer(required=False,source='client_to_bill')
    mainCarrierObj = CarrierSerializer(required=False,source='main_carrier')
    class Meta:
        model = ReceptionOrder
        fields = [  'status','number','creation_date','employee','issued_by','issued_byObj','destination_agent','destination_agentObj','shipper','shipperObj','consignee', 'consigneeObj','client_to_bill','clientBillObj','main_carrier','mainCarrierObj','commodities','events','attachments']
