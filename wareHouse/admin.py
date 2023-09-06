from django.contrib import admin
from wareHouse.models import pickUpOrder, pieces, shipper, issuedBy, pickUpLocation, consignee, deliveryLocation


from import_export import resources
from import_export.admin import ImportExportModelAdmin

######################## Classes assigned for import/export. HERE ############################## 

class pickUpOrderResource(resources.ModelResource):
    class Meta:
        model = pickUpOrder

class piecesResource(resources.ModelResource):
    class Meta:
        model = pieces

         
# Register your models here.

@admin.register(shipper)
class wareHouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'customerName',
                    'vendorName',
                    'agentName'
                ]

@admin.register(issuedBy)
class wareHouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'forWardingAgents',
                    'forWardingAgents',
                ]

@admin.register(pickUpLocation)
class wareHouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'customerName',
                    'vendorName',
                    'agentName'
                ]

@admin.register(consignee)
class wareHouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'customerName',
                    'vendorName',
                    'agentName',
                    'carrierName'
                ]
    
@admin.register(deliveryLocation)
class wareHouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'customerName',
                    'vendorName',
                    'agentName',
                    'carrierName'
                ]

@admin.register(pickUpOrder)
class wareHouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'status',
                    'number',
                    'creationDate',
                    'pickUpDate',
                    'deliveryDate',
                    'date',
                    'issuedByKey',
                    'destinationAgentKey',
                    'employeekey',
                    'shipperkey',
                    'PickUpLocationkey',
                    'consigneekey',
                    'deliveryLocationkey',
                    'inlandCarrierKey',
                    'mainCarrierKey',
                    'proNumber',
                    'trackingNumber',
                    'supplierKey',
                    'invoiceNumber',
                    'purchaseOrderNum'
                ]
    resource_class = pickUpOrderResource

@admin.register(pieces)
class wareHouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
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
    resource_class = piecesResource


