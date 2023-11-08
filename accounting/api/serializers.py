from rest_framework import serializers
from accounting.models import chartAccounts, ItemServices, openingBalance, invoice

class chartAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model   = chartAccounts
        fields  = ['id', 
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
        fields   = ['id', 
                    'code', 
                    'description', 
                    'accountName', 
                    'type', 'amount', 
                    'autCreation', 
                    'currency', 
                    'iataCode',
                    ]

class openingBalanceSerializer(serializers.ModelSerializer):
    class Meta :
        model   = openingBalance
        fields   = ['id', 
                    'name',
                    'balance',
                    ]

class invoiceSerializer(serializers.ModelSerializer):
    class Meta :
        model   = invoice
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

                    ]