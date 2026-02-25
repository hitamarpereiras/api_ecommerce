from rest_framework import viewsets
from banners.models import Banner
from banners.serializers import BannerSerializer


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
