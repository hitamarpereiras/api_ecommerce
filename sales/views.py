from rest_framework import viewsets
from sales.models import Sale
from sales.serializers import SaleSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsOwnerOfSale


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('-created_at')
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated, IsOwnerOfSale]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(account__user=user)
