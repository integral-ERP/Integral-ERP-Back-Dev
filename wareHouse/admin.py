from django.contrib import admin
from wareHouse.models import pickUpOrder
# ---------------------------------------
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Import - Export Data Model

class pickUpOrderResource(resources.ModelResource):
    class Meta:
        model = pickUpOrder
        
# Register your models here.

@admin.register(pickUpOrder)
class wareHouseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id',
                    'status',
                    'number',
                    'date',
                    'shipper',
                    'consignee',
                    'PickUpOrder',
                    'deliveryName',
                    'piedes',
                    'carrier',
                    'weight',
                    'volume',
                    ]
    resource_class = pickUpOrderResource 