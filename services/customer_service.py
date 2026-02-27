from django.contrib.auth.models import User
from django.db import transaction

from customers.models import Customer
from services.img_service import process_image
from services.supabase_service import upload_image


class CustomerService:

    @staticmethod
    @transaction.atomic
    def register_customer(validated_data):
        
        #Cria User + Customer, processa imagem e atualiza os campos adicionais
        
        image = validated_data.pop("image", None)
        username = validated_data.pop("username")
        password = validated_data.pop("password")

        # Criar User
        user = User.objects.create_user(
            username=username,
            password=password
        )

        # Criar Customer
        customer = Customer.objects.create(
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
                bucket="clientes"
            )

            # 3.3 ➤ atualizar a account
            customer.avatar_url = avatar_url
            customer.save()

        return customer