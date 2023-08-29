from rest_framework.routers import DefaultRouter
from wareHouse.api.views import pickUpOrdereApiViewSet

router_wareHouse = DefaultRouter()

router_wareHouse.register(prefix='pickUpOrder', basename='pickUpOrder', viewset=pickUpOrdereApiViewSet)

