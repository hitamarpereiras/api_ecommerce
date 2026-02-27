from rest_framework import viewsets
from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response


from services.img_service import process_image
from services.supabase_service import upload_image


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]

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
