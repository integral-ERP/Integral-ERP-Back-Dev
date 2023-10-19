from rest_framework import serializers
from configuration.models import paymentTerms

class paymentTermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = paymentTerms
        fields = [ 'id',
                    'description',
                    'dueDays',
                    'discountPercentage',
                    'discountDays',
                    'inactive',
      ]