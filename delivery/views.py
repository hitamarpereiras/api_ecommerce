from rest_framework import viewsets
from delivery.models import DeliveryMan
from delivery.serializers import DeliveryManSerializer


class DeliveryManViewSet(viewsets.ModelViewSet):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManSerializer
