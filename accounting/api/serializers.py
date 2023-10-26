from rest_framework import serializers
from accounting.models import chartAccounts, ItemServices, openingBalance

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