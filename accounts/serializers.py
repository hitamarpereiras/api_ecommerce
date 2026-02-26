from rest_framework import serializers
from accounts.models import Account

class AccountLogoUploadSerializer(serializers.Serializer):
    logo = serializers.ImageField()

class AccountSerializer(serializers.ModelSerializer):
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
            'created_at',
            'updated_at',
        ]