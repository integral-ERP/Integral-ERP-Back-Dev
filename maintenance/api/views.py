from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from maintenance.models import Carrier,Agent,Vendor,Customer,Employee,Port,PackageType,Location,Company,Shipper,PickUpLocation,Consignee,DeliveryLocation,ClientToBill, ReleasedTo
from maintenance.api.serializers import CarrierSerializer,AgentSerializer,VendorSerializer,CustomerSerializer,EmployeeSerializer,PortSerializer,PackageTypeSerializer,LocationSerializer,CompanySerializer,ShipperSerializer,PickUpLocationSerializer,ConsigneeSerializer,DeliveryLocationSerializer,ClientToBillSerializer, ReleasedToSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

class BaseModelViewSet(ModelViewSet):
    disabled_field = 'disabled'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        setattr(instance, self.disabled_field, True)
        instance.save()
        return Response(data = instance,status=status.HTTP_200_OK)

class CarrierApiViewSet(BaseModelViewSet):
    serializer_class = CarrierSerializer
    queryset = Carrier.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

class AgentApiViewSet(BaseModelViewSet):
    serializer_class = AgentSerializer
    queryset = Agent.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

class VendorApiViewSet(BaseModelViewSet):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CustomerApiViewSet(BaseModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

class EmployeeApiViewSet(BaseModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']
    
class PortApiViewSet(BaseModelViewSet):
    serializer_class = PortSerializer
    queryset = Port.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['code','name','method','country','sub_division','used','remarks','maritime','rail','road','air','mail','border_crossing','us_customs_code']

class PackageTypeApiViewSet(BaseModelViewSet):
    serializer_class = PackageTypeSerializer
    queryset = PackageType.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['description','length','height','width','weight','volume','max_weight','type','type_code','container_code','container_type','ground','air','ocean']

class LocationApiViewSet(BaseModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['status','code','description','empty','type','zone','length','width','height','volume','weight','max_weight','disabled']
    

class CompanyApiViewSet(BaseModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','website','account_number','contact_first_name','contact_last_name','identification_number','division','street_and_number','city','state','country','zip_code','port',
                    'type_logistic_provider','type_distribution','type_airline_carrier','type_ocean_carrier','type_company_warehouse','company_iata_code','company_fmc_code','company_scac_code','company_tsa_code','company_img_name','company_img_logo']
    
class ShipperApiViewSet(BaseModelViewSet):
    serializer_class = ShipperSerializer
    queryset = Shipper.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer','vendor','agent']


class PickUpLocationApiViewSet(BaseModelViewSet):
    serializer_class = PickUpLocationSerializer
    queryset = PickUpLocation.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer','vendor','agent']

class ConsigneeApiViewSet(BaseModelViewSet):
    serializer_class = ConsigneeSerializer
    queryset = Consignee.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer','vendor','agent','carrier']
    pagination_class = PageNumberPagination
    page_size = 10 

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class DeliveryLocationApiViewSet(BaseModelViewSet):
    serializer_class = DeliveryLocationSerializer
    queryset = DeliveryLocation.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer','vendor','agent','carrier']

class ClientToBillApiViewSet(BaseModelViewSet):
    serializer_class = ClientToBillSerializer
    queryset = ClientToBill.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['shipper','consignee']

class ReleasedToApiViewSet(BaseModelViewSet):
    serializer_class = ReleasedToSerializer
    queryset = ReleasedTo.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'customer', 'vendor', 'agent', 'carrier']    