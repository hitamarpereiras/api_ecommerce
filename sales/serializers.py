from rest_framework import serializers
from sales.models import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = [
            'id',
            'total',
            'subtotal',
            'remaining',
            'payment_method',
            'rate_delivery',
            'account',
            'order',
            'status',
            'collaborator',
            'observation',
            'created_at',
            'updated_at',
        ]