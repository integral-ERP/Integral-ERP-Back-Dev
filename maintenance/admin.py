from django.contrib import admin
from maintenance.models import carrier, port, vendor, employee,company, address, companyType, companyInfo, addressInfo, companyLogo, companyRegisCode, systCurren, importSchedule, packType, forWardingAgents, containerCode, containerEquipType, containerType, customer, location, wareHouseProviders, consignee

from import_export import resources
from import_export.admin import ImportExportModelAdmin

##################### Classes assigned for import/export HERE #####################

class carrierResource(resources.ModelResource):
    class Meta:
        model = carrier

class portResource(resources.ModelResource):
    class Meta:
        model = port

class vendorResource(resources.ModelResource):
    class Meta:
        model = vendor

class employeeResource(resources.ModelResource):
    class Meta:
        model = employee

class companyResource(resources.ModelResource):
    class Meta:
        model = company

class addressResource(resources.ModelResource):
    class Meta:
        model = address

class companyTypeResource(resources.ModelResource):
    class Meta:
        model = companyType

class companyInfoResource(resources.ModelResource):
    class Meta:
        model = companyInfo

class addressInfoResource(resources.ModelResource):
    class Meta:
        model = addressInfo

class companyLogoResource(resources.ModelResource):
    class Meta:
        model = companyLogo

class companyRegisCodeResource(resources.ModelResource):
    class Meta:
        model = companyRegisCode

class systCurrenResource(resources.ModelResource):
    class Meta:
        model = systCurren

class importScheduleResource(resources.ModelResource):
    class Meta:
        model = importSchedule

class packTypeResource(resources.ModelResource):
    class Meta:
        model = packType

class wareHouseProvidersResource(resources.ModelResource):
    class Meta:
        model = wareHouseProviders

class forWardingAgentsResource(resources.ModelResource):
    class Meta:
        model = forWardingAgents

class containerTypeResource(resources.ModelResource):
    class Meta:
        model = containerType

class customerResource(resources.ModelResource):
    class Meta:
        model = customer

class locationResource(resources.ModelResource):
    class Meta:
        model = location

class containerCodeResource(resources.ModelResource):
    class Meta:
        model = containerCode

class containerEquipTypeResource(resources.ModelResource):
    class Meta:
        model = containerEquipType

class consigneeResource(resources.ModelResource):
    class Meta:
        model = consignee


################### Register your models here. #########################

@admin.register(carrier)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
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
    resource_class = carrierResource 

@admin.register(port)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
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
    resource_class = portResource 

@admin.register(vendor)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
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
                    ]
    resource_class = vendorResource 
    
@admin.register(employee)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
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
    resource_class = employeeResource


@admin.register (company)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
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
    resource_class = companyResource

@admin.register (address)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
                    'streetNumber', 
                    'city', 
                    'country', 
                    'state', 
                    'zipCode', 
                    'port'
                ]
    resource_class = addressResource

@admin.register (companyType)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
                    'logisticsProvi', 
                    'distribution', 
                    'airlineCarrier', 
                    'oceanCarrier', 
                    'companyWarehouse'
                ]
    resource_class = companyTypeResource

@admin.register (companyInfo)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
                    'nameCompany', 
                    'phone', 
                    'fax', 
                    'email', 
                    'webSide', 
                    'firstNameContac', 
                    'lasNameContac'
                ]
    resource_class = companyInfoResource

@admin.register (addressInfo)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
                    'streetNumber', 
                    'city', 
                    'country', 
                    'state', 
                    'zipCode'
                ]
    resource_class = addressInfoResource

@admin.register (companyLogo)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
                    'imgName', 
                    'imgLogo'
                ]
    resource_class = companyLogoResource

@admin.register (companyRegisCode)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
                    'iataCode', 
                    'fmc', 
                    'scacCodeUs', 
                    'tsaNumber'
                ]
    resource_class = companyRegisCode

@admin.register (systCurren)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
                    'localCurrency', 
                    'companyMoreCurren'
                ]
    resource_class = systCurrenResource

@admin.register (importSchedule)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        list_display = ['id',
                        'schedulesB', 
                        'schedulesD',
                        'schedulesK'
                        ]
        resource_class = importScheduleResource

@admin.register (packType)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        list_display = [    'id',
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
        resource_class = packTypeResource

@admin.register(wareHouseProviders)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
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
    resource_class = wareHouseProvidersResource

@admin.register(forWardingAgents)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
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
    resource_class = forWardingAgentsResource

@admin.register(containerType)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'type',
                    'description',
                    'containerCode',
                    'containerType',
                    'ground',
                    'air',
                    'ocean'
                ]
    resource_class = containerTypeResource

@admin.register(customer)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
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
resource_class = customerResource

@admin.register(location)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
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
    resource_class = locationResource

@admin.register(containerCode)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'code',
                    'description'
                ]
    resource_class = containerCodeResource
    
@admin.register(containerEquipType)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'code',
                    'description'
                ]
    resource_class = containerEquipTypeResource

@admin.register(consignee)
class maintenanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'customerId',
                    'vendorId',
                    'forwarAgentId'
                ]
    resource_class = consigneeResource

    