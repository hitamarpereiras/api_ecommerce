from django.contrib.auth.models import User
from django.db import transaction

from accounts.models import Account
from services.img_service import process_image
from services.supabase_service import upload_image
from services.get_colors_service import get_this_colors

class AccountService:

    @staticmethod
    @transaction.atomic
    def register_account(validated_data):
        
        #Cria User + Account, processa imagem e atualiza os campos adicionais
        
        image = validated_data.pop("image", None)
        username = validated_data.pop("username")
        password = validated_data.pop("password")

        # Criar User
        user = User.objects.create_user(
            username=username,
            password=password
        )

        # Criar Account
        account = Account.objects.create(
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

            # 3.2 ➤ gerar paleta de cor
            palette = get_this_colors(buffer)

            # 3.3 ➤ atualizar a account
            account.avatar_url = avatar_url
            account.color_palette = palette
            account.save()

        return account