from django.contrib import admin
from wareHouse.models import PickUpOrder,Shipper, pieces


from import_export import resources
from import_export.admin import ImportExportModelAdmin

######################## Classes assigned for import/export. HERE ############################## 

class PickUpOrderResource(resources.ModelResource):
    class Meta:
        model = PickUpOrder

class ShipperResource(resources.ModelResource):
    class Meta:
        model = Shipper

class piecesResource(resources.ModelResource):
    class Meta:
        model = pieces

# Register your models here.

@admin.register(PickUpOrder)
class wareHouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['status','number','creation_date','pick_up_date','delivery_date','date','issued_by','destination_agent','employee','shipper','pick_up_location','consignee','delivery_location','inland_carrier','main_carrier','pro_number','tracking_number','supplier','invoice_number','purchase_order_number'
                ]
    resource_class = PickUpOrderResource

@admin.register(Shipper)
class wareHouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['customer','agent','vendor'
                ]
    resource_class = ShipperResource

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


