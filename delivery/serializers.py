from rest_framework import serializers
from delivery.models import DeliveryMan


class DeliveryManSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = [
            'id',
            'name',
            'cpf',
            'phone',
            'plate',
            'vehicle_type',
            'color',
            'avatar_url',
            'total_deliveries',
            'is_available',
            'account',
            'created_at',
            'updated_at',
        ]