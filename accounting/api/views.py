from rest_framework.viewsets import ModelViewSet
from accounting.models import  ChartAccounts, ItemServices, OpeningBalance, Invoice, Payments
from accounting.api.serializers import  ChartAccountsSerializer, ItemServicesSerializer, OpeningBalanceSerializer, InvoiceSerializer, PaymentsSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

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

class PaymentsApiViewSet(ModelViewSet):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    
    @api_view(['GET'])
    def filter_invoices_by_account_id(request, account_id):
        invoices = Invoice.objects.filter(accountById=account_id)
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)