from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'customer',
            'name_customer',
            'phone',
            'observation',
            'address',
            'latitude',
            'longitude',
            'house_number',
            'total',
            'subtotal',
            'remaining',
            'payment_method',
            'rate_delivery',
            'delivery_man',
            'code',
            'created_at',
            'itens',
            'status',
        ]