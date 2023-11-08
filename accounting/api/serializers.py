from rest_framework import serializers
from accounting.models import ChartAccounts, ItemServices, OpeningBalance, Invoice

class ChartAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model   = ChartAccounts
        fields  = [ 'id', 
                    'name', 
                    'type', 
                    'referenceNum', 
                    'balanceUSD', 
                    'currency', 
                    'parentAccount',
                    'accountNumber',
                    'note',
                    ]
 
class ItemServicesSerializer(serializers.ModelSerializer):
    class Meta :
        model   = ItemServices
        fields  = ['id', 
                    'code', 
                    'description', 
                    'accountName', 
                    'type', 'amount', 
                    'autCreation', 
                    'currency', 
                    'iataCode',
                    ]

class OpeningBalanceSerializer(serializers.ModelSerializer):
    class Meta :
        model   = OpeningBalance
        fields  = ['id', 
                    'name',
                    'balance',
                    ]

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta :
        model   = Invoice
        fields   = ['id', 
                    'number',
                    'account',
                    'paymentTem',
                    'division',
                    'apply',
                    'due',
                    'trasaDate',
                    'bilingAddres',
                    'paidAdd',
                    'exchangeRate',
                    'amount',
                    'taxCode',
                    'totalAmount',
                    'amountDue',
                    'invoiceCharges',
                    'amount',
                    'taxCode',
                    'amountDue',
                    'charges',
                    'currency',
                    'issuedById',
                    'issuedByName',
                    'paymentById',
                    'paymentByDesc',
                    'accountById',
                    'accountByName',
                    'accountByType',
                    'accounten',
                    ]