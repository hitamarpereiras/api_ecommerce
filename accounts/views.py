from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from accounts.models import Account
from accounts.serializers import AccountSerializer, AccountLogoUploadSerializer

from services.img_service import process_image
from services.supabase_service import upload_image
from services.get_colors_service import get_this_colors


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @action(
        detail=False,
        methods=["post"],
        parser_classes=[MultiPartParser, FormParser],
        url_path="upload-logo"
    )
    def upload_logo(self, request):

        serializer = AccountLogoUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = serializer.validated_data["logo"]

        account = request.user.accounts

        # Processa imagem
        buffer, ext = process_image(image, 300, 300)

        # Upload para Supabase
        avatar_url = upload_image(
            file_bytes=buffer.getvalue(),
            ext=ext,
            bucket="avatars"
        )

        # Extrai paleta de cores
        palette = get_this_colors(buffer)

        # Atualiza model
        account.avatar_url = avatar_url
        account.color_palette = palette
        account.save()

        return Response({
            "avatar_url": avatar_url,
            "color_palette": palette
        }, status=status.HTTP_200_OK)
