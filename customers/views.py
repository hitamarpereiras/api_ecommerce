from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from customers.models import Customer

from customers.serializers import CustomerSerializer, RegisterCustomerSerializer
from services.customer_service import CustomerService
from rest_framework.parsers import MultiPartParser, FormParser
from core.permissions import OnlyTheOwnerCustomer

from services.img_service import process_image
from services.supabase_service import upload_image
from rest_framework import status


class CustomerRgisterView(APIView):
    permission_classes = []
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = RegisterCustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # serve para chamar o serviço de criação de cliente
        CustomerService.register_customer(serializer.validated_data)

        return Response(
            {"message": "Usuário criado com sucesso"},
            status=status.HTTP_201_CREATED
        )
 

class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        avatar = request.FILES.get("image")

        # Atualiza campos normais
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Se veio imagem → processa
        if avatar:
            buffer, ext = process_image(avatar, 300, 300)

            avatar_url = upload_image(
                file_bytes=buffer.getvalue(),
                ext=ext,
                bucket="clientes"
            )

            instance.avatar_url = avatar_url
            instance.save()

        return Response(
            {"message": "Usuário atualizado com sucesso"},
            status=status.HTTP_200_OK
        )
