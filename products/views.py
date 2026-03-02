from rest_framework import viewsets
from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response
from core.permissions import OnlyTheOwnerAccount


from services.img_service import process_image
from services.supabase_service import upload_image


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [OnlyTheOwnerAccount]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['category', 'price', 'account']
    search_fields = ['name']
    ordering_fields = ['price', 'updated_at']

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(account__user=user)

    def create(self, request, *args, **kwargs):
        image_product = request.FILES.get("image")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image_url = None

        if image_product:
            buffer, ext = process_image(image_product, 1024, 1024)

            image_url = upload_image(
                file_bytes=buffer.getvalue(),
                ext=ext,
                bucket="produtos"
            )

        # salvando com a url
        product = serializer.save(image_url=image_url)

        return Response(
            {"message": "Produto criado com sucesso"},
            status=status.HTTP_201_CREATED
        )

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        image_product = request.FILES.get("image")

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if image_product:
            buffer, ext = process_image(image_product, 1024, 1024)

            image_url = upload_image(
                file_bytes=buffer.getvalue(),
                ext=ext,
                bucket="produtos"
            )

            instance.image_url = image_url

        serializer.save()

        return Response(
            {"message": "Produto atualizado com sucesso"},
            status=status.HTTP_200_OK
        )
