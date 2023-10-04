from rest_framework.routers import DefaultRouter

from wareHouse.api.views import  PickUpOrderApiViewSet, ReceptionOrderApiViewSet

router_wareHouse = DefaultRouter()

router_wareHouse.register(prefix='pickUpOrder', basename='pickUpOrder', viewset=PickUpOrderApiViewSet)
router_wareHouse.register(prefix='receptionOrder', basename='receptionOrder', viewset=ReceptionOrderApiViewSet)


