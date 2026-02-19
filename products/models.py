from django.db import models
from accounts.models import Account

class Category(models.TextChoices):
        DRINK = 'bebidas', 'bebidas'
        CANDY = 'doces', 'doces'
        SALTY = 'salgados', 'salgados'
        OTHER = 'outros', 'outros'
        EXCLUSIVE = 'exclusivo', 'exclusivo'

class Product(models.Model):
        id_account = models.ForeignKey(
            Account,
            on_delete=models.CASCADE,
            verbose_name='Conta ID'
        )
        name = models.CharField(max_length=100)
        category = models.CharField(
                choices=Category.choices,
                default=Category.CANDY,
                verbose_name='Categoria',
                db_index=True
        )
        description = models.TextField(
                default='Produto sem descrição',
                max_length=320,
                verbose_name='Descrição'
        )
        price = models.DecimalField(
                default=0,
                max_digits=10,
                decimal_places=2,
                verbose_name='Preço'
        )
        stock = models.IntegerField(
                default=0,
                verbose_name='Estoque'
        )
        image_url = models.URLField(
            blank=True,
            null=True,
            verbose_name='URL da Imagem'
        )
        crop_x = models.IntegerField(
            blank=True, 
            null=True,
            verbose_name='Eixo x'
        )
        crop_y = models.IntegerField(
            blank=True, 
            null=True,
            verbose_name='Eixo y'
        )
        crop_width = models.IntegerField(
            blank=True, 
            null=True,
            verbose_name='Corte Largura'
        )
        crop_height = models.IntegerField(
            blank=True, 
            null=True,
            verbose_name='Corte Altura'
        )
        created_at = models.DateTimeField(
            auto_now_add=True,
            verbose_name='Criado em',
        )
        updated_at = models.DateTimeField(
            auto_now=True,
            verbose_name='Atualizado em',
        )