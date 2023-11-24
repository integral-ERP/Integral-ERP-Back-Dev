from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from configuration.models import PaymentTerms
from configuration.api.serializers import PaymentTermsSerializer

class PaymentTermsViewSet(ModelViewSet):
    serializer_class = PaymentTermsSerializer
    queryset = PaymentTerms.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = [
                    'id',
                    'description',
                    'dueDays',
                    'discountPercentage',
                    'discountDays',
                    'inactive', 
                ]