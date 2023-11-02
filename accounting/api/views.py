from rest_framework.viewsets import ModelViewSet
from accounting.models import  chartAccounts, ItemServices, openingBalance, invoice
from accounting.api.serializers import  chartAccountsSerializer, ItemServicesSerializer, openingBalanceSerializer, invoiceSerializer

class chartAccountsApiViewSet(ModelViewSet):
    serializer_class = chartAccountsSerializer
    queryset = chartAccounts.objects.all()

class ItemServicesApiViewSet(ModelViewSet):
    serializer_class = ItemServicesSerializer
    queryset = ItemServices.objects.all()
    
class openingBalanceApiViewSet(ModelViewSet):
    serializer_class = openingBalanceSerializer
    queryset = openingBalance.objects.all()

class invoiceApiViewSet(ModelViewSet):
    serializer_class =invoiceSerializer
    queryset = invoice.objects.all()
