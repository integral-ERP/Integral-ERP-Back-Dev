from rest_framework.viewsets import ModelViewSet
from accounting.models import  ChartAccounts, ItemServices, OpeningBalance, Invoice
from accounting.api.serializers import  ChartAccountsSerializer, ItemServicesSerializer, OpeningBalanceSerializer, InvoiceSerializer

class ChartAccountsApiViewSet(ModelViewSet):
    serializer_class = ChartAccountsSerializer
    queryset = ChartAccounts.objects.all()

class ItemServicesApiViewSet(ModelViewSet):
    serializer_class = ItemServicesSerializer
    queryset = ItemServices.objects.all()
    
class OpeningBalanceApiViewSet(ModelViewSet):
    serializer_class = OpeningBalanceSerializer
    queryset = OpeningBalance.objects.all()

class InvoiceApiViewSet(ModelViewSet):
    serializer_class =InvoiceSerializer
    queryset = Invoice.objects.all()
