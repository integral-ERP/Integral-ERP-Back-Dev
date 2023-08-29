from rest_framework.viewsets import ModelViewSet
from wareHouse.models import pickUpOrder
from wareHouse.api.serializers import pickUpOrderSerializer


class pickUpOrdereApiViewSet(ModelViewSet):
    serializer_class = pickUpOrderSerializer
    queryset = pickUpOrder.objects.all()

