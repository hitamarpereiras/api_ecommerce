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


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'account',
            'name',
            'category',
            'description',
            'price',
            'stock',
            'image_url',
            'crop_x',
            'crop_y',
            'crop_width',
            'crop_height',
            'created_at',
            'updated_at',
        ]