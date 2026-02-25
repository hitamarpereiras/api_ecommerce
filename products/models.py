from django.db import models
from accounts.models import Account

class Category(models.Model):
        name = models.CharField(
            max_length=50,
            unique=True,
            verbose_name='Categoria'
        )
        description = models.TextField(
            default='Categoria sem descrição',
            max_length=320,
            verbose_name='Descrição',
        )
        created_at = models.DateTimeField(
            auto_now_add=True,
            verbose_name='Criado em',
        )
        updated_at = models.DateTimeField(
            auto_now=True,
            verbose_name='Atualizado em',
        )

        class Meta:
            verbose_name = 'Categoria'
            verbose_name_plural = 'Categorias'

        def __str__(self):
            return self.name
        
class Product(models.Model):
        account = models.ForeignKey(
            Account,
            blank=True,
            null=True,
            on_delete=models.CASCADE,
            verbose_name='Conta',
            db_index=True
        )
        name = models.CharField(max_length=100)
        category = models.CharField(
                max_length=50,
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

        class Meta:
            verbose_name = 'Produto'
            verbose_name_plural = 'Produtos'

        def __str__(self):
            return self.name