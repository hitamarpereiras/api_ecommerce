from rest_framework import viewsets
from orders.models import Order
from orders.serializers import OrderSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
