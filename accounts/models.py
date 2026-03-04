from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name='account',
        verbose_name='Conta'
    )
    name = models.CharField(max_length=100, verbose_name='Nome')
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone'
    )
    address = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Endereço'
    )
    cnpj = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='CNPJ'
    )
    avatar_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Avatar URL'
    )
    instagram_url = models.URLField(
        blank=True, 
        null=True
    )
    facebook_url = models.URLField(
        blank=True, 
        null=True
    )
    other_url = models.URLField(
        blank=True, 
        null=True
    )
    color_palette = models.JSONField(
        blank=True,
        null=True,
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
        ordering = ['-created_at']
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'

    def __str__(self):
        return f"{self.name}"