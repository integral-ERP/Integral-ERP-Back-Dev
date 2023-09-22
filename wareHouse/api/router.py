from rest_framework.routers import DefaultRouter

from wareHouse.api.views import  pickUpOrderApiViewSet, piecesApiViewSet

router_wareHouse = DefaultRouter()

router_wareHouse.register(prefix='pickUpOrder', basename='pickUpOrder', viewset=pickUpOrderApiViewSet)
router_wareHouse.register(prefix='pieces', basename='pieces', viewset=piecesApiViewSet)
