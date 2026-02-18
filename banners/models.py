from django.db import models
from accounts.models import Account


class Banner(models.Model):
    id_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name='Banner'
    )
    name = models.CharField(max_length=100)
    banner_url = models.URLField(
        blank=True,
        null=True,
    )
    link = models.URLField(
        blank=True,
        null=True
    )
    value_publi = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    crop_x = models.IntegerField(
        blank=True, 
        null=True
    )
    crop_y = models.IntegerField(
        blank=True, 
        null=True
    )
    crop_width = models.IntegerField(
        blank=True, 
        null=True
    )
    crop_height = models.IntegerField(
        blank=True, 
        null=True
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
