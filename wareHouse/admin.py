from django.contrib import admin
from wareHouse.models import pickUpOrder, pieces

# ---------------Import/Export------------------------
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#Classes assigned for import/export. here
class pickUpOrderResource(resources.ModelResource):
    class Meta:
        model = pickUpOrder

class piecesResource(resources.ModelResource):
    class Meta:
        model = pieces

        
# Register your models here.

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
                    'inlandCarrier',
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
