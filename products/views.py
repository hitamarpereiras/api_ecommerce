from rest_framework import viewsets
from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from products.tasks import process_and_upload_image

from services.validators import validate_image
from services.img_service import process_image
from services.supabase_service import upload_image


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'account']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Category.objects.filter(account=self.request.user.account)
        
        return Category.objects.all().order_by('-updated_at')
    
    def perform_create(self, serializer):
        serializer.save(account=self.request.user.account)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        
        return [IsAuthenticated()]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-updated_at')
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'price', 'account']

    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return Product.objects.all().order_by('-created_at')

        return Product.objects.filter(account=self.request.user.account)
    


    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        
        return [IsAuthenticated()]



    def create(self, request, *args, **kwargs):
        image_product = request.FILES.get("image")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account = request.user.account

        # salva primeiro SEM imagem
        product = serializer.save(
            account=account,
            image_url=None
        )

        if image_product:
            validate_image(image_product)

            # envia pra fila (não bloqueia)
            process_and_upload_image.delay(
                product.id,
                image_product.read()
            )

        return Response(
            {
                "message": "Produto criado com sucesso",
                "id": product.id
            },
            status=status.HTTP_201_CREATED
        )


    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        image_product = request.FILES.get("image")

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        if image_product:
            validate_image(image_product)

            process_and_upload_image.delay(
                instance.id,
                image_product.read()
            )

        return Response(
            {"message": "Produto atualizado com sucesso"},
            status=status.HTTP_200_OK
        )