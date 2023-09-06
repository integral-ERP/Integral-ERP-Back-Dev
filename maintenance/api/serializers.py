from rest_framework import serializers
from maintenance.models import carrier, port, vendor, employee,company, address, companyType, companyInfo, addressInfo, companyLogo, companyRegisCode, systCurren, importSchedule, packType, wareHouseProviders, forWardingAgents, containerCode, containerEquipType, containerType, customer, location, consignee

from drf_extra_fields.fields import Base64ImageField

class carrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = carrier
        fields = [  'id',
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
                    'passengerOnlyAirline'
                  ]

class portSerializer(serializers.ModelSerializer):
    class Meta:
        model = port
        fields = [  'id',
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
                    'usCustomsCode',
                  ]

class vendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor
        fields = [  'id',
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
                    'streetNumber',
                    'city',
                    'state',
                    'country',
                    'zipCode',
                  ]
        
class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = [  'id',
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
                    'zipCode'
                  ]
        
class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = [  'id', 
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
                    'idNetWord'
                ]

class addresSerializer(serializers.ModelSerializer):
    class Meta:
        model = address
        fields = [  'id', 
                    'streetNumber', 
                    'city', 
                    'country', 
                    'state', 
                    'zipCode', 
                    'port'
                ]

class companyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = companyType
        fields = [  'id', 
                    'logisticsProvi', 
                    'distribution', 
                    'airlineCarrier', 
                    'oceanCarrier', 
                    'companyWarehouse'
                ]

class companyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = companyInfo
        fields = [  'id', 
                    'nameCompany', 
                    'phone', 
                    'fax', 
                    'email', 
                    'webSide', 
                    'firstNameContac', 
                    'lasNameContac'
                ]

class addressInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = addressInfo
        fields = [  'id', 
                    'streetNumber',
                    'city', 
                    'country', 
                    'state', 
                    'zipCode'
                ]

class companyLogoSerializer(serializers.ModelSerializer):
    imgLogo = Base64ImageField(required=False)
    class Meta:
        model = companyLogo
        fields = [  'id', 
                  'imgName', 
                  'imgLogo'
                ]

class companyRegisCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = companyRegisCode
        fields = [ 'id', 
                    'iataCode', 
                    'fmc', 
                    'scacCodeUs', 
                    'tsaNumber'
                ]

class systCurrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = systCurren
        fields = [ 'id', 
                    'localCurrency', 
                    'companyMoreCurren'
                ]

class importScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = importSchedule
        fields = [  'id', 
                    'schedulesB', 
                    'schedulesD', 
                    'schedulesK'
                ]

class packTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = packType
        fields = [  'id',
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
                    'ocean'
                ]
        
class wareHouseProvidersSerializer(serializers.ModelSerializer):
    class Meta:
        model = wareHouseProviders
        fields = [  'id',
                    'name',
                    'phone',
                    'mobilePhone',
                    'email',
                    'fax',
                    'webSide',
                    'referentNumber',
                    'firstNameContac',
                    'lasNameContac',
                    'streetNumber',
                    'city',
                    'state',
                    'country',
                    'zipCode'
                ]

class forWardingAgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = forWardingAgents
        fields = [  'id',
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
                    'zipCode'
                ]

class containerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = containerType
        fields = [  'id',
                    'type',
                    'description',
                    'containerCode',
                    'containerType',
                    'ground',
                    'air',
                    'ocean'
                ]

class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = [  'id',
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
                    'TypePerson'
                ]

class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = location
        fields = [  'id',
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
                    'disable'
                ]

class containerCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = containerCode
        fields = [  'id',
                    'code',
                    'description'
                ]

class containerEquipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = containerEquipType
        fields = [  'id',
                    'code',
                    'description'
                ]

class consigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = consignee
        fields = ['id',
                    'customerId',
                    'vendorId',
                    'forwarAgentId'
                ]

