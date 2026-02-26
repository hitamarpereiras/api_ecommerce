from rest_framework import serializers
from banners.models import Banner

class BannerSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, write_only=True)

    class Meta:
        model = Banner
        fields = [
            'id',
            'account',
            'name',
            'banner_url',
            'link',
            'value_publi',
            'crop_x',
            'crop_y',
            'crop_width',
            'crop_height',
            'status',
            'image',
            'created_at',
            'updated_at',
        ]

    def create(self, validated_data):
        validated_data.pop("image", None)
        return super().create(validated_data)
        
    def update(self, instance, validated_data):
        validated_data.pop("image", None)
        return super().update(instance, validated_data)