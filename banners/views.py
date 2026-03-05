from rest_framework import viewsets
from banners.models import Banner
from banners.serializers import BannerSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsOwnerOfBanner

from services.img_service import process_image
from services.supabase_service import upload_image
from django_filters.rest_framework import DjangoFilterBackend


class BannerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOfBanner]
    queryset = Banner.objects.all().order_by('-created_at')
    serializer_class = BannerSerializer
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(account__user=user)


    def create(self, request, *args, **kwargs):
        banner_image = request.FILES.get("image")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        banner_url = None

        if banner_image:
            buffer, ext = process_image(banner_image, 1200, 675)

            banner_url = upload_image(
                file_bytes=buffer.getvalue(),
                ext=ext,
                bucket="banners"
            )

        # salvando com a url
        banner = serializer.save(banner_url=banner_url)

        return Response(
            {"message": "Banner criado com sucesso"},
            status=status.HTTP_201_CREATED
        )

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        banner_image = request.FILES.get("image")

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if banner_image:
            buffer, ext = process_image(banner_image, 1200, 675)

            banner_url = upload_image(
                file_bytes=buffer.getvalue(),
                ext=ext,
                bucket="banners"
            )

            instance.banner_url = banner_url

        serializer.save()

        return Response(
            {"message": "Banner atualizado com sucesso"},
            status=status.HTTP_200_OK
        )
