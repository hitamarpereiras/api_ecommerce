from celery import shared_task
from services.img_service import process_image
from services.supabase_service import upload_image
from products.models import Product


@shared_task(bind=True, max_retries=3)
def process_and_upload_image(self, product_id, image_bytes):
    try:
        from io import BytesIO

        image = BytesIO(image_bytes)

        buffer, ext = process_image(image, 1024, 1024)

        image_url = upload_image(
            file_bytes=buffer.getvalue(),
            ext=ext,
            bucket="produtos"
        )

        product = Product.objects.get(id=product_id)
        product.image_url = image_url
        product.save()

    except Exception as e:
        raise self.retry(exc=e, countdown=5)