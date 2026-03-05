from rest_framework import serializers
from delivery.models import DeliveryMan


class RegisterDeliveryManSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    name = serializers.CharField()
    cpf = serializers.CharField(required=False, allow_blank=True)
    phone = serializers.CharField(required=False, allow_blank=True)
    plate = serializers.CharField(required=False, allow_blank=True)
    vehicle_type = serializers.CharField(required=False, allow_blank=True)
    color = serializers.CharField(required=False, allow_blank=True)

    image = serializers.ImageField(required=False, write_only=True)



class DeliveryManSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, write_only=True)

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
            'image',
            'account',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['avatar_url', 'created_at', 'updated_at']

    """Sobrescreve os métodos create e update para remover 
    o campo "image" antes de criar ou atualizar a instância"""

    def create(self, validated_data):
        validated_data.pop("image", None)
        return super().create(validated_data)
        
    def update(self, instance, validated_data):
        validated_data.pop("image", None)
        return super().update(instance, validated_data)