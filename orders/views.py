from rest_framework import viewsets
from orders.models import Order
from orders.serializers import OrderSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from core.permissions import OnlyTheOwnerCustomer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions, OnlyTheOwnerCustomer]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(customer__user=user)