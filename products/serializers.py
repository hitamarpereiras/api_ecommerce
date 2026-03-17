from rest_framework import serializers
from products.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['account']


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'description',
            'price',
            'stock',
            'image_url',
            'image',
            'crop_x',
            'crop_y',
            'crop_width',
            'crop_height',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['image_url', 'account']

    def create(self, validated_data):
        validated_data.pop('image', None)
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data.pop('image', None)
        return super().update(instance, validated_data)