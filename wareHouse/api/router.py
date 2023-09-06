from rest_framework.routers import DefaultRouter

from wareHouse.api.views import shipperApiViewSet, issuedByApiViewSet, pickUpLocationApiViewSet, consigneeApiViewSet, deliveryLocationApiViewSet, pickUpOrderApiViewSet, piecesApiViewSet

router_wareHouse = DefaultRouter()
 
router_wareHouse.register(prefix='shipper', basename='shipper', viewset=shipperApiViewSet)
router_wareHouse.register(prefix='issuedBy', basename='issuedBy', viewset=issuedByApiViewSet)
router_wareHouse.register(prefix='pickUpLocation', basename='pickUpLocation', viewset=pickUpLocationApiViewSet)
router_wareHouse.register(prefix='consignee', basename='consignee', viewset=consigneeApiViewSet)
router_wareHouse.register(prefix='deliveryLocation', basename='deliveryLocation', viewset=deliveryLocationApiViewSet)
router_wareHouse.register(prefix='pickUpOrder', basename='pickUpOrder', viewset=pickUpOrderApiViewSet)
router_wareHouse.register(prefix='pieces', basename='pieces', viewset=piecesApiViewSet)
