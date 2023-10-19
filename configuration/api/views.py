from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from configuration.models import paymentTerms
from configuration.api.serializers import paymentTermsSerializer

class paymentTermsViewSet(ModelViewSet):
    serializer_class = paymentTermsSerializer
    queryset = paymentTerms.objects.all()