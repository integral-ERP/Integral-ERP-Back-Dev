from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from maintenance.models import Carrier,Agent,Vendor,Customer,Employee,Port,PackageType,Location,Company,Shipper,PickUpLocation,Consignee,DeliveryLocation,ClientToBill, ReleasedTo
from maintenance.api.serializers import CarrierSerializer,AgentSerializer,VendorSerializer,CustomerSerializer,EmployeeSerializer,PortSerializer,PackageTypeSerializer,LocationSerializer,CompanySerializer,ShipperSerializer,PickUpLocationSerializer,ConsigneeSerializer,DeliveryLocationSerializer,ClientToBillSerializer, ReleasedToSerializer
from rest_framework.response import Response
from rest_framework import status

class BaseModelViewSet(ModelViewSet):
    disabled_field = 'disabled'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        setattr(instance, self.disabled_field, True)
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CarrierApiViewSet(BaseModelViewSet):
    serializer_class = CarrierSerializer
    queryset = Carrier.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AgentApiViewSet(BaseModelViewSet):
    serializer_class = AgentSerializer
    queryset = Agent.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VendorApiViewSet(BaseModelViewSet):
    serializer_class = VendorSerializer
    queryset = Vendor.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerApiViewSet(BaseModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeApiViewSet(BaseModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','fax','website','reference_number','contact_first_name','contact_last_name','identification_number','identification_type','street_and_number','city','state','country','zip_code','type_person']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PortApiViewSet(BaseModelViewSet):
    serializer_class = PortSerializer
    queryset = Port.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['code','name','method','country','sub_division','used','remarks','maritime','rail','road','air','mail','border_crossing','us_customs_code']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PackageTypeApiViewSet(BaseModelViewSet):
    serializer_class = PackageTypeSerializer
    queryset = PackageType.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['description','length','height','width','weight','volume','max_weight','type','type_code','container_code','container_type','ground','air','ocean']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LocationApiViewSet(BaseModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['status','code','description','empty','type','zone','length','width','height','volume','weight','max_weight','disabled']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CompanyApiViewSet(BaseModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','phone','mobile_phone','email','website','account_number','contact_first_name','contact_last_name','identification_number','division','street_and_number','city','state','country','zip_code','port',
                    'type_logistic_provider','type_distribution','type_airline_carrier','type_ocean_carrier','type_company_warehouse','company_iata_code','company_fmc_code','company_scac_code','company_tsa_code','company_img_name','company_img_logo']
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ShipperApiViewSet(BaseModelViewSet):
    serializer_class = ShipperSerializer
    queryset = Shipper.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer','vendor','agent']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PickUpLocationApiViewSet(BaseModelViewSet):
    serializer_class = PickUpLocationSerializer
    queryset = PickUpLocation.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer','vendor','agent']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ConsigneeApiViewSet(BaseModelViewSet):
    serializer_class = ConsigneeSerializer
    queryset = Consignee.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer','vendor','agent','carrier']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DeliveryLocationApiViewSet(BaseModelViewSet):
    serializer_class = DeliveryLocationSerializer
    queryset = DeliveryLocation.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer','vendor','agent','carrier']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClientToBillApiViewSet(BaseModelViewSet):
    serializer_class = ClientToBillSerializer
    queryset = ClientToBill.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['shipper','consignee']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReleasedToApiViewSet(BaseModelViewSet):
    serializer_class = ReleasedToSerializer
    queryset = ReleasedTo.objects.filter(disabled=False)
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'customer', 'vendor', 'agent', 'carrier']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.disabled = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)