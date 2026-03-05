from django.contrib.auth.models import User
from django.db import transaction

from delivery.models import DeliveryMan
from services.img_service import process_image
from services.supabase_service import upload_image


class DeliveryManService:

    @staticmethod
    @transaction.atomic
    def register_deliveryman(validated_data):
        
        #Cria User + DeliveryMan, processa imagem e atualiza os campos adicionais
        
        image = validated_data.pop("image", None)
        username = validated_data.pop("username")
        password = validated_data.pop("password")

        # Criar User
        user = User.objects.create_user(
            username=username,
            password=password
        )

        # Criar DeliveryMan
        customer = DeliveryMan.objects.create(
            user=user,
            **validated_data
        )

        # Se tiver imagem ➤ processar imagem
        if image:
            buffer, ext = process_image(image, 300, 300)

            # 3.1 ➤ subir para Supabase, recebe URL
            avatar_url = upload_image(
                file_bytes=buffer.getvalue(),
                ext=ext,
                bucket="avatars"
            )

            # 3.3 ➤ atualizar a account
            customer.avatar_url = avatar_url
            customer.save()

        return customer