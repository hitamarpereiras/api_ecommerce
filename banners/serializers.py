from rest_framework import serializers
from banners.models import Banner

class BannerSerializer(serializers.ModelSerializer):
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
            'created_at',
            'updated_at',
        ]