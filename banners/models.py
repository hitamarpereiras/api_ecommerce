from django.db import models
from accounts.models import Account


class Banner(models.Model):
    id_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name='Conta ID'
    )
    name = models.CharField(max_length=100)
    banner_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='URL do Banner'
    )
    link = models.URLField(
        blank=True,
        null=True
    )
    value_publi = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Valor da Publicação'
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
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em',
    )
