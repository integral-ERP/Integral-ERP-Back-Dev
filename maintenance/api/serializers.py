from rest_framework import serializers
from maintenance.models import Carrier,Agent,Vendor,Customer,Employee,Port,PackageType,Location,Company,Shipper,PickUpLocation,Consignee,DeliveryLocation

from drf_extra_fields.fields import Base64ImageField

class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ['id','name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id','name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ['id','code','name','method','country','sub_division','used','remarks','maritime','rail','road','air','mail','border_crossing','us_customs_code']
class PackageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageType
        fields = ['id','description','length','height','width','weight','volume','max_weight','type','type_code','container_code','container_type','ground','air','ocean']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id','status','code','description','empty','type','zone','length','width','height','volume','weight','max_weight','disabled']

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ['id','name','phone','mobile_phone','email','website','account_number','contact_first_name','contact_last_name','identification_number','division','street_and_number','city','state','country','zip_code','port',
                    'type_logistic_provider','type_distribution','type_airline_carrier','type_ocean_carrier','type_company_warehouse','company_iata_code','company_fmc_code','company_scac_code','company_tsa_code','company_img_name','company_img_logo']       
        

class ShipperSerializer(serializers.ModelSerializer):
    customerid = serializers.CharField(max_length=200, required=False, allow_null=True)
    vendorid = serializers.CharField(max_length=200, required=False, allow_null=True)
    agentid = serializers.CharField(max_length=200, required=False, allow_null=True)

    class Meta:
        model = Shipper
        fields = ['id', 'customer', 'vendor', 'agent', 'customerid', 'vendorid', 'agentid', 'data']

    def create(self, validated_data):
        customer_id = validated_data.pop('customerid', None)
        vendor_id = validated_data.pop('vendorid', None)
        agent_id = validated_data.pop('agentid', None)

        # Buscar los objetos correspondientes en las tablas respectivas
        customer = None
        vendor = None
        agent = None

        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                pass

        if vendor_id:
            try:
                vendor = Vendor.objects.get(id=vendor_id)
            except Vendor.DoesNotExist:
                pass

        if agent_id:
            try:
                agent = Agent.objects.get(id=agent_id)
            except Agent.DoesNotExist:
                pass

        # Almacena los datos recuperados como una propiedad JSON
        shipperObj = None
        if(customer):
            shipperObj = CustomerSerializer(customer).data
        if(vendor):
            shipperObj = VendorSerializer(vendor).data
        if(agent):
            shipperObj = AgentSerializer(shipper).data
        data = {
            'obj': shipperObj
        }

        # Crea el objeto Shipper con los datos proporcionados
        shipper = Shipper.objects.create(**validated_data)

        # Almacenar los datos JSON en un campo separado
        shipper.data = data
        shipper.save()

        return shipper

class PickUpLocationSerializer(serializers.ModelSerializer):
    customerid = serializers.CharField(max_length=200, required=False, allow_null=True)
    vendorid = serializers.CharField(max_length=200, required=False, allow_null=True)
    agentid = serializers.CharField(max_length=200, required=False, allow_null=True)

    class Meta:
        model = PickUpLocation
        fields = ['id', 'customer', 'vendor', 'agent', 'customerid', 'vendorid', 'agentid', 'data']

    def create(self, validated_data):
        customer_id = validated_data.pop('customerid', None)
        vendor_id = validated_data.pop('vendorid', None)
        agent_id = validated_data.pop('agentid', None)

        # Buscar los objetos correspondientes en las tablas respectivas
        customer = None
        vendor = None
        agent = None

        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                pass

        if vendor_id:
            try:
                vendor = Vendor.objects.get(id=vendor_id)
            except Vendor.DoesNotExist:
                pass

        if agent_id:
            try:
                agent = Agent.objects.get(id=agent_id)
            except Agent.DoesNotExist:
                pass

        # Almacena los datos recuperados como una propiedad JSON
        shipperObj = None
        if(customer):
            shipperObj = CustomerSerializer(customer).data
        if(vendor):
            shipperObj = VendorSerializer(vendor).data
        if(agent):
            shipperObj = AgentSerializer(shipper).data
        data = {
            'obj': shipperObj
        }

        # Crea el objeto Shipper con los datos proporcionados
        shipper = PickUpLocation.objects.create(**validated_data)

        # Almacenar los datos JSON en un campo separado
        shipper.data = data
        shipper.save()

        return shipper

class ConsigneeSerializer(serializers.ModelSerializer):
    customerid = serializers.CharField(max_length=200, required=False, allow_null=True)
    vendorid = serializers.CharField(max_length=200, required=False, allow_null=True)
    agentid = serializers.CharField(max_length=200, required=False, allow_null=True)
    carrierid = serializers.CharField(max_length=200, required=False, allow_null=True)
    class Meta:
        model = Consignee
        fields = ['id', 'customer', 'vendor', 'agent','carrier', 'customerid', 'vendorid', 'agentid', 'carrierid', 'data']

    def create(self, validated_data):
        customer_id = validated_data.pop('customerid', None)
        vendor_id = validated_data.pop('vendorid', None)
        agent_id = validated_data.pop('agentid', None)
        carrier_id = validated_data.pop('carrierid', None)

        # Buscar los objetos correspondientes en las tablas respectivas
        customer = None
        vendor = None
        agent = None
        carrier = None

        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                pass

        if vendor_id:
            try:
                vendor = Vendor.objects.get(id=vendor_id)
            except Vendor.DoesNotExist:
                pass

        if agent_id:
            try:
                agent = Agent.objects.get(id=agent_id)
            except Agent.DoesNotExist:
                pass

        if carrier_id:
            try:
                carrier = Carrier.objects.get(id=carrier_id)
            except Carrier.DoesNotExist:
                pass

                # Almacena los datos recuperados como una propiedad JSON
        shipperObj = None
        if(customer):
            shipperObj = CustomerSerializer(customer).data
        if(vendor):
            shipperObj = VendorSerializer(vendor).data
        if(agent):
            shipperObj = AgentSerializer(agent).data
        if(carrier):
            shipperObj = CarrierSerializer(carrier).data
        data = {
            'obj': shipperObj
        }

        # Crea el objeto Shipper con los datos proporcionados
        consignee = Consignee.objects.create(**validated_data)

        # Almacenar los datos JSON en un campo separado
        consignee.data = data
        consignee.save()

        return consignee

class DeliveryLocationSerializer(serializers.ModelSerializer):
    customerid = serializers.CharField(max_length=200, required=False, allow_null=True)
    vendorid = serializers.CharField(max_length=200, required=False, allow_null=True)
    agentid = serializers.CharField(max_length=200, required=False, allow_null=True)
    carrierid = serializers.CharField(max_length=200, required=False, allow_null=True)
    class Meta:
        model = DeliveryLocation
        fields = ['id', 'customer', 'vendor', 'agent','carrier', 'customerid', 'vendorid', 'agentid', 'carrierid', 'data']

    def create(self, validated_data):
        customer_id = validated_data.pop('customerid', None)
        vendor_id = validated_data.pop('vendorid', None)
        agent_id = validated_data.pop('agentid', None)
        carrier_id = validated_data.pop('carrierid', None)

        # Buscar los objetos correspondientes en las tablas respectivas
        customer = None
        vendor = None
        agent = None
        carrier = None

        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                pass

        if vendor_id:
            try:
                vendor = Vendor.objects.get(id=vendor_id)
            except Vendor.DoesNotExist:
                pass

        if agent_id:
            try:
                agent = Agent.objects.get(id=agent_id)
            except Agent.DoesNotExist:
                pass

        if carrier_id:
            try:
                carrier = Carrier.objects.get(id=carrier_id)
            except Carrier.DoesNotExist:
                pass

        shipperObj = None
        if(customer):
            shipperObj = CustomerSerializer(customer).data
        if(vendor):
            shipperObj = VendorSerializer(vendor).data
        if(agent):
            shipperObj = AgentSerializer(agent).data
        if(carrier):
            shipperObj = CarrierSerializer(carrier).data
        data = {
            'obj': shipperObj
        }

        # Crea el objeto Shipper con los datos proporcionados
        shipper = DeliveryLocation.objects.create(**validated_data)

        # Almacenar los datos JSON en un campo separado
        shipper.data = data
        shipper.save()

        return shipper
