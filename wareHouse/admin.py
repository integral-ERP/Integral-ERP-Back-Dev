from django.contrib import admin
from wareHouse.models import PickUpOrder, ReceptionOrder


from import_export import resources
from import_export.admin import ImportExportModelAdmin

######################## Classes assigned for import/export. HERE ############################## 

class PickUpOrderResource(resources.ModelResource):
    class Meta:
        model = PickUpOrder

class ReceptionOrderResource(resources.ModelResource):
    class Meta:
        model = ReceptionOrder
# Register your models here.

@admin.register(PickUpOrder)
class wareHouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'status',
                    'number',
                    'creation_date',
                    'pick_up_date',
                    'delivery_date',
                    'date',
                    'issued_by',
                    'destination_agent',
                    'employee',
                    'shipper',
                    'pick_up_location',
                    'consignee',
                    'delivery_location',
                    'inland_carrier',
                    'main_carrier',
                    'pro_number',
                    'tracking_number',
                    'supplier',
                    'invoice_number',
                    'purchase_order_number'
                ]
    resource_class = PickUpOrderResource


@admin.register(ReceptionOrder)
class wareHouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'status',
                    'number',
                    'creation_date',
                    'employee',
                    'issued_by',
                    'destination_agent',
                    'shipper',
                    'consignee',
                    'client_to_bill',
                    'main_carrier',
                    'commodities',
                    'events',
                    'attachments'
                ]
    resource_class = ReceptionOrderResource



