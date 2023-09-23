from rest_framework.viewsets import ModelViewSet
from accounting.models import chartAccounts, ItemServices, openingBalance
from accounting.api.serializers import chartAccountsSerializer, ItemServicesSerializer, openingBalanceSerializer

class chartAccountsApiViewSet(ModelViewSet):
    serializer_class = chartAccountsSerializer
    queryset = chartAccounts.objects.all()

class ItemServicesApiViewSet(ModelViewSet):
    serializer_class = ItemServicesSerializer
    queryset = ItemServices.objects.all()
    
class openingBalanceApiViewSet(ModelViewSet):
    serializer_class = openingBalanceSerializer
    queryset = openingBalance.objects.all()


    