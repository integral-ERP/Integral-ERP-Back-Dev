from rest_framework.routers import DefaultRouter

from wareHouse.api.views import  PickUpOrderApiViewSet, piecesApiViewSet, ShipperApiViewSet

router_wareHouse = DefaultRouter()

router_wareHouse.register(prefix='pickUpOrder', basename='pickUpOrder', viewset=PickUpOrderApiViewSet)
router_wareHouse.register(prefix='pieces', basename='pieces', viewset=piecesApiViewSet)
router_wareHouse.register(prefix='shipper', basename='shipper', viewset=ShipperApiViewSet)
