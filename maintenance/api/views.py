from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from maintenance.models import Carrier,Agent,Vendor,Customer,Employee,Port,PackageType,Location,Company
from maintenance.api.serializers import CarrierSerializer,AgentSerializer,VendorSerializer,CustomerSerializer,EmployeeSerializer,PortSerializer,PackageTypeSerializer,LocationSerializer,CompanySerializer


class CarrierApiViewSet(ModelViewSet):
    serializer_class = CarrierSerializer
    queryset = Carrier.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

class AgentApiViewSet(ModelViewSet):
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

class VendorApiViewSet(ModelViewSet):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

class CustomerApiViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

class EmployeeApiViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']
    
class PortApiViewSet(ModelViewSet):
    serializer_class = PortSerializer
    queryset = Port.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['code','name','method','country','sub_division','used','remarks','maritime','rail','road','air','mail','border_crossing','us_customs_code']

class PackageTypeApiViewSet(ModelViewSet):
    serializer_class = PackageTypeSerializer
    queryset = PackageType.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['description','length','height','width','weight','volume','max_weight','type','type_code','container_code','container_type','ground','air','ocean']

class LocationApiViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['status','code','description','empty','type','zone','length','width','height','volume','weight','max_weight','disabled']

class CompanyApiViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','website','account_number','contact_first_name','contact_last_name','identification_number','division','street_and_number','city','state','country','zip_code','port',
                    'type_logistic_provider','type_distribution','type_airline_carrier','type_ocean_carrier','type_company_warehouse','company_iata_code','company_fmc_code','company_scac_code','company_tsa_code','company_img_name','company_img_logo']