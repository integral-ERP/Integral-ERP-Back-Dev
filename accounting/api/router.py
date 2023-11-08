from rest_framework.routers import DefaultRouter
from accounting.api.views import  ChartAccountsApiViewSet, ItemServicesApiViewSet, OpeningBalanceApiViewSet, InvoiceApiViewSet

router_accounting = DefaultRouter()

router_accounting.register(prefix='ChartAccounts', basename='ChartAccounts', viewset=ChartAccountsApiViewSet)
router_accounting.register(prefix='ItemServices', basename='ItemServices', viewset=ItemServicesApiViewSet)
router_accounting.register(prefix='OpeningBalance', basename='OpeningBalance', viewset=OpeningBalanceApiViewSet)
router_accounting.register(prefix='Invoice', basename='Invoice', viewset=InvoiceApiViewSet)