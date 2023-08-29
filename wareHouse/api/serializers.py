from rest_framework import serializers
from wareHouse.models import pickUpOrder



class pickUpOrderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = pickUpOrder
        fields = [  'id',
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
