from django.contrib import admin
from accounting.models import  ChartAccounts, ItemServices, OpeningBalance, Invoice, Payments

# ---------------Import/Export------------------------
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#Classes assigned for import/export. here

class ChartAccountsResource(resources.ModelResource):
    class Meta:
        model = ChartAccounts

class ItemServicesResource(resources.ModelResource):
    class Meta:
        model = ItemServices

class OpeningBalanceResource(resources.ModelResource):
    class Meta:
        model = OpeningBalance

class InvoiceResource(resources.ModelResource):
    class Meta:
        model = Invoice

class PaymentsResource(resources.ModelResource):
    class Meta:
        model = Payments

# Register your models here.

@admin.register (ChartAccounts)
class accountingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
                    'name',  
                    'type', 
                    'referenceNum', 
                    'balanceUSD', 
                    'currency', 
                    'parentAccount',
                    'accountNumber',
                    'note',
                    'typeChart',
                    ] 
    resource_class = ChartAccountsResource
     

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
    
    
@admin.register (OpeningBalance)
class accountingAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
                    'name',
                    'balance'
                    ]
    resource_class = OpeningBalanceResource

@admin.register (Invoice)
class invoiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
                    'number',
                    'account',
                    'paymentTem',
                    'division',
                    'apply',        #verificar y borrar
                    'due',
                    'trasaDate',
                    'bilingAddres',
                    'paidAdd',
                    'exchangeRate',
                    'invoiceCharges',
                    'currency',
                    'issued_by',
                    'issuedByName',
                    'paymentById',
                    'paymentByDesc',
                    'accountById',
                    'accountByName',
                    'accountByType',
                    ]
    resource_class = InvoiceResource

@admin.register (Payments)
class PaymentsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 
                    'customerById',
                    'customerByName',
                    'amountReceived',
                    'trasaDate',
                    # 'transaction_Date',
                    'number',
                    'memo',
                    'inviceData',
                    ]
    resource_class = PaymentsResource