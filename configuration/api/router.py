from rest_framework.routers import DefaultRouter
from configuration.api.views import paymentTermsViewSet

router_configuration = DefaultRouter()

router_configuration.register(prefix='paymentTerms', basename='paymentTerms', viewset=paymentTermsViewSet)
