from django.contrib import admin
from accounting.models import chartAccounts, ItemServices, openingBalance

# ---------------Import/Export------------------------
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#Classes assigned for import/export. here

class chartAccountsResource(resources.ModelResource):
    class Meta:
        model = chartAccounts

class ItemServicesResource(resources.ModelResource):
    class Meta:
        model = ItemServices

class openingBalanceResource(resources.ModelResource):
    class Meta:
        model = openingBalance

# Register your models here.

@admin.register (chartAccounts)
class accountingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
                    'name',  
                    'type', 
                    'referenceNum', 
                    'balanceUSD', 
                    'currency', 
                    'parentAccount'
                    ] 
     

@admin.register (ItemServices)
class accountingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
                    'code', 
                    'description', 
                    'accountName', 
                    'type', 'amount', 
                    'autCreation', 
                    'currency', 
                    'iataCode'
                    ]
    resource_class = ItemServicesResource
    
    
@admin.register (openingBalance)
class accountingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
                    'name',
                    'balance'
                    ]
    resource_class = openingBalanceResource
    
