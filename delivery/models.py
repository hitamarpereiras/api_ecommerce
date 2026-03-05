from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account

class VehicleType(models.TextChoices):
        MOTO = 'moto', 'Moto'
        CARRO = 'carro', 'Carro'
        BICICLETA = 'bicicleta', 'Bicicleta'
        VAN = 'van', 'Van'
        OUTRO = 'outro', 'Outro'

class DeliveryMan(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name='delivery',
        verbose_name='Entregador'
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
        unique=True,
        verbose_name='Placa'
    )
    vehicle_type = models.CharField(
        max_length=20,
        choices=VehicleType.choices,
        default=VehicleType.MOTO,
        verbose_name='Tipo de Veículo'
    )
    color = models.CharField(
        blank=True,
        null=True,
        max_length=15,
        verbose_name='Cor do Veículo'
    )
    avatar_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Avatar URL'
    )
    total_deliveries = models.IntegerField(
          default=0,
          verbose_name='Tota de entregas'
    )
    is_available = models.BooleanField(
        default=False,
        verbose_name='Disponível'
    )
    account = models.ForeignKey(
        Account,
        null=True,
        blank=True,
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

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Entregador'
        verbose_name_plural = 'Entregadores'

    def __str__(self):
        return f"{self.name}"

