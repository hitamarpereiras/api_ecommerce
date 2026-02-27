from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Account

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    name = serializers.CharField()
    phone = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    cnpj = serializers.CharField(required=False, allow_blank=True)

    image = serializers.ImageField(required=False)

class AccountSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, write_only=True)

    class Meta:
        model = Account
        fields = [
            'id',
            'name',
            'phone',
            'address',
            'cnpj',
            'avatar_url',
            'instagram_url',
            'facebook_url',
            'other_url',
            'color_palette',
            'image',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['avatar_url', 'color_palette', 'created_at', 'updated_at']

    """Sobrescreve os métodos create e update para remover 
    o campo "image" antes de criar ou atualizar a instância"""

    def create(self, validated_data):
        validated_data.pop("image", None)
        return super().create(validated_data)
        
    def update(self, instance, validated_data):
        validated_data.pop("image", None)
        return super().update(instance, validated_data)