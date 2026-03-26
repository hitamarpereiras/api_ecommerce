from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from accounts.models import Account
from services.validators import validate_image
from accounts.serializers import AccountSerializer, RegisterSerializer

from services.img_service import process_image
from services.supabase_service import upload_image
from services.get_colors_service import get_this_colors
from services.account_service import AccountService


class RegisterView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # serve para chamar o serviço de criação de conta
        AccountService.register_account(serializer.validated_data)

        return Response(
            {"message": "Usuário criado com sucesso"},
            status=status.HTTP_201_CREATED
        )


class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Account.objects.filter(user=user)
        return Account.objects.none()

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        logo = request.FILES.get("image")

        # Atualiza campos normais
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)


        if logo:
            validate_image(logo) # Validar antes de processar

            buffer, ext = process_image(logo, 300, 300)

            avatar_url = upload_image(
                file_bytes=buffer.getvalue(),
                ext=ext,
                bucket="avatars"
            )

            palette = get_this_colors(buffer)

            instance.avatar_url = avatar_url
            instance.color_palette = palette
            instance.save()

        return Response(
            {"message": "Usuário atualizados com sucesso"},
            status=status.HTTP_200_OK
        )
