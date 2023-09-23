from rest_framework.routers import DefaultRouter
from accounting.api.views import chartAccountsApiViewSet, ItemServicesApiViewSet, openingBalanceApiViewSet

router_accounting = DefaultRouter()

router_accounting.register(prefix='chartAccounts', basename='chartAccounts', viewset=chartAccountsApiViewSet)
router_accounting.register(prefix='ItemServices', basename='ItemServices', viewset=ItemServicesApiViewSet)
router_accounting.register(prefix='openingBalance', basename='openingBalance', viewset=openingBalanceApiViewSet)