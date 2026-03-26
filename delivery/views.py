from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from delivery.models import DeliveryMan
from delivery.serializers import DeliveryManSerializer, RegisterDeliveryManSerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from services.validators import validate_image
from services.img_service import process_image
from services.supabase_service import upload_image
from services.delivery_service import DeliveryManService


class RegisterView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = RegisterDeliveryManSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # serve para chamar o serviço de criação de conta
        DeliveryManService.register_deliveryman(serializer.validated_data)

        return Response(
            {"message": "Usuário criado com sucesso"},
            status=status.HTTP_201_CREATED
        )


class DeliveryManViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DeliveryMan.objects.all().order_by("-created_at")
    serializer_class = DeliveryManSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return DeliveryMan.objects.filter(id=user.id)
        return DeliveryMan.objects.none()


    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        image = request.FILES.get("image")

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Se veio imagem → processa
        if image:
            validate_image(image)

            buffer, ext = process_image(image, 300, 300)

            avatar_url = upload_image(
                file_bytes=buffer.getvalue(),
                ext=ext,
                bucket="avatars"
            )

            instance.avatar_url = avatar_url
            instance.save()

        return Response(
            {"message": "Usuário atualizados com sucesso"},
            status=status.HTTP_200_OK
        )