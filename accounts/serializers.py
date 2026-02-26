from rest_framework import serializers
from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(required=False, write_only=True)

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
            'logo',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['avatar_url', 'color_palette', 'created_at', 'updated_at']
        
    def update(self, instance, validated_data):
        validated_data.pop("logo", None)
        return super().update(instance, validated_data)