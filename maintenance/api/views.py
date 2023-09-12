from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from maintenance.models import carrier, port, vendor, employee, company, address, companyType, addressInfo, companyLogo, companyRegisCode, systCurren, importSchedule, companyInfo, packType, wareHouseProviders, forWardingAgents, containerType, customer, location, containerCode, containerEquipType, consignee
from maintenance.api.serializers import carrierSerializer, portSerializer, vendorSerializer, employeeSerializer, companySerializer, addresSerializer, companyTypeSerializer, companyInfoSerializer, addressInfoSerializer, companyLogoSerializer, companyRegisCodeSerializer, systCurrenSerializer, importScheduleSerializer, packTypeSerializer, wareHouseProvidersSerializer, forWardingAgentsSerializer, containerTypeSerializer, customerSerializer, locationSerializer, containerCodeSerializer, containerEquipTypeSerializer, consigneeSerializer


class carrierApiViewSet(ModelViewSet):
    serializer_class = carrierSerializer
    queryset = carrier.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [ 'id',
                    'name',
                    'phone',
                    'movelPhone',
                    'email',
                    'fax',
                    'webSide',
                    'referentNumber',
                    'firstNameContac',
                    'lasNameContac',
                    'numIdentification',
                    'typeIdentificacion',
                    'sistenID',
                    'streetNumber',
                    'city',
                    'state',
                    'country',
                    'zipCode',
                    'parentAccount',
                    'carrierType',
                    'methodCode',
                    'carrierCode',
                    'scacNumber',
                    'iataCode',
                    'airlineCode',
                    'airlinePrefix',
                    'airwayBillNumbers',
                    'passengerOnlyAirline']

  
    
    

class portApiViewSet(ModelViewSet):
    serializer_class = portSerializer
    queryset = port.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [ 'id',
                    'code',
                    'name',
                    'method',
                    'country',
                    'subdivision',
                    'used',
                    'remarks',
                    'maritime',
                    'rail',
                    'road',
                    'air',
                    'mail',
                    'borderCrossing',
                    'usCustomsCode']

class vendorApiViewSet(ModelViewSet):
    serializer_class = vendorSerializer
    queryset = vendor.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [ 'id',
                    'name',
                    'phone',
                    'movelPhone',
                    'email',
                    'fax',
                    'webSide',
                    'referentNumber',
                    'firstNameContac',
                    'lasNameContac',
                    'numIdentification',
                    'typeIdentificacion',
                    'sistenID',
                    'streetNumber',
                    'city',
                    'state',
                    'country',
                    'zipCode',]

class employeeApiViewSet(ModelViewSet):
    serializer_class = employeeSerializer
    queryset = employee.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id',
                    'name',
                    'phone',
                    'movelPhone',
                    'email',
                    'fax',
                    'webSide',
                    'referentNumber',
                    'firstNameContac',
                    'lasNameContac',
                    'numIdentification',
                    'typeIdentificacion',
                    'sistenID',
                    'streetNumber',
                    'city',
                    'state',
                    'country',
                    'zipCode' ]

class companyApiViewSet(ModelViewSet):
    serializer_class = companySerializer
    queryset = company.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 
                    'nameCompany', 
                    'firstNameContac', 
                    'lasNameContac', 
                    'numIdentification', 
                    'idEntity', 
                    'email',
                    'webSide',
                    'numCuent',
                    'firstNameContac',
                    'lasNameContac',
                    'numIdentification',
                    'division',
                    'idNetWord']

class addressApiViewSet(ModelViewSet):
    serializer_class = addresSerializer
    queryset = address.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 
                    'streetNumber', 
                    'city', 
                    'country', 
                    'state', 
                    'zipCode', 
                    'port']

class companyTypeApiViewSet(ModelViewSet):
    serializer_class = companyTypeSerializer
    queryset = companyType.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 
                    'logisticsProvi', 
                    'distribution', 
                    'airlineCarrier', 
                    'oceanCarrier', 
                    'companyWarehouse']


class companyInfoApiViewSet(ModelViewSet):
    serializer_class = companyInfoSerializer
    queryset = companyInfo.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 
                    'nameCompany', 
                    'phone', 
                    'fax', 
                    'email', 
                    'webSide', 
                    'firstNameContac', 
                    'lasNameContac']

class addressInfoApiViewSet(ModelViewSet):
    serializer_class = addressInfoSerializer
    queryset = addressInfo.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 
                    'streetNumber', 
                    'city', 
                    'country', 
                    'state', 
                    'zipCode']

class companyLogoApiViewSet(ModelViewSet):
    serializer_class = companyLogoSerializer
    queryset = companyLogo.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 
                    'imgName', 
                    'imgLogo']

class companyRegisCodeApiViewSet(ModelViewSet):
    serializer_class = companyRegisCodeSerializer
    queryset = companyRegisCode.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 
                    'iataCode', 
                    'fmc', 
                    'scacCodeUs', 
                    'tsaNumber']

class systCurrenApiViewSet(ModelViewSet):
    serializer_class = systCurrenSerializer
    queryset = systCurren.objects.all()
    

class importScheduleApiViewSet(ModelViewSet):
    serializer_class = importScheduleSerializer
    queryset = importSchedule.objects.all()

class packTypeApiViewSet(ModelViewSet):
    serializer_class = packTypeSerializer
    queryset = packType.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [  'id',
                            'description',
                            'length',
                            'height',
                            'width',  
                            'weight',
                            'volume',
                            'maxWeight',
                            'type',
                            'typeCode',
                            'containerCode',
                            'containerType',
                            'ground',
                            'air',
                            'ocean']

class wareHouseProvidersApiViewSet(ModelViewSet):
    serializer_class = wareHouseProvidersSerializer
    queryset = wareHouseProviders.objects.all()

class forWardingAgentsApiViewSet(ModelViewSet):
    serializer_class = forWardingAgentsSerializer
    queryset = forWardingAgents.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [  'id',
                    'name',
                    'phone',
                    'movelPhone',
                    'email',
                    'fax',
                    'webSide',
                    'referentNumber',
                    'firstNameContac',
                    'lasNameContac',
                    'numIdentification',
                    'typeIdentificacion',
                    'sistenID',
                    'streetNumber',
                    'city',
                    'state',
                    'country',
                    'zipCode']

class containerTypeApiViewSet(ModelViewSet):
    serializer_class = containerTypeSerializer
    queryset = containerType.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [ 'id',
                    'type',
                    'description',
                    'containerCode',
                    'containerType',
                    'ground',
                    'air',
                    'ocean']

    
class customerApiViewSet(ModelViewSet):
    serializer_class = customerSerializer
    queryset = customer.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [ 'id',
                    'name',
                    'phone',
                    'mobilePhone',
                    'email',
                    'fax',
                    'webSide',
                    'referentNumber',
                    'firstNameContac',
                    'lasNameContac',
                    'numIdentification',
                    'typeIdentificacion',
                    'streetNumber',
                    'sistenID',
                    'city',
                    'state',
                    'country',
                    'zipCode',
                    'TypePerson']

class locationApiViewSet(ModelViewSet):
    serializer_class = locationSerializer
    queryset = location.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [ 'id',
                    'status',
                    'code',
                    'description',
                    'empty',
                    'type',
                    'zone',
                    'length',
                    'width',
                    'height',
                    'volume',
                    'weight',
                    'maxWeight',
                    'disable']

class containerCodeApiViewSet(ModelViewSet):
    serializer_class = containerCodeSerializer
    queryset = containerCode.objects.all()

class containerEquipTypeApiViewSet(ModelViewSet):
    serializer_class = containerEquipTypeSerializer
    queryset = containerEquipType.objects.all()
    
class consigneeApiViewSet(ModelViewSet):
    serializer_class = consigneeSerializer
    queryset = consignee.objects.all()