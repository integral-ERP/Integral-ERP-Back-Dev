from rest_framework import serializers
from maintenance.models import Carrier,Agent,Vendor,Customer,Employee,Port,PackageType,Location,Company

from drf_extra_fields.fields import Base64ImageField

class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ('name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person')

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person')

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person')

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ('code','name','method','country','sub_division','used','remarks','maritime','rail','road','air','mail','border_crossing','us_customs_code')
class PackageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageType
        fields = ('description','length','height','width','weight','volume','max_weight','type','type_code','container_code','container_type','ground','air','ocean')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('status','code','description','empty','type','zone','length','width','height','volume','weight','max_weight','disabled')

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ('name','phone','mobile_phone','email','website','account_number','contact_first_name','contact_last_name','identification_number','division','street_and_number','city','state','country','zip_code','port',
                    'type_logistic_provider','type_distribution','type_airline_carrier','type_ocean_carrier','type_company_warehouse','company_iata_code','company_fmc_code','company_scac_code','company_tsa_code','company_img_name','company_img_logo')




