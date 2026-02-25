from rest_framework import serializers
from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'name',
            'phone',
            'address',
            'house_number',
            'coins',
            'avatar_url',
            'created_at',
            'updated_at',
        ]