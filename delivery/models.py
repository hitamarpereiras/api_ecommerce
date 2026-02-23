from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account


class DeliveryMan(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name='delivery_profile'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Nome'
    )
    cpf = models.CharField(
        blank=True,
        null=True,
        max_length=14,
        verbose_name='CPF'
    )
    phone = models.CharField(
        blank=True,
        null=True,
        max_length=15,
        verbose_name='Telefone'
    )
    plate = models.CharField(
        blank=True,
        null=True,
        max_length=8,
        verbose_name='Placa'
    )
    vehicle_type = models.CharField(
        blank=True,
        null=True,
        verbose_name='Tipo de Veículo'
    )
    color = models.CharField(
        blank=True,
        null=True,
        max_length=15,
        verbose_name='Cor do Veículo'
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        verbose_name='Conta'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em',
    )

