from django.db import models
from customers.models import Customer


class Shopping(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        verbose_name='Cliente ID',
    )
    itens = models.JSONField(
        blank=True,
        null=True,
        verbose_name='Itens'
    )
    subtotal = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        verbose_name='Subotal'
    )
    rate_delivery = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        verbose_name='Taxa de Entrega'
    )
    total = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        verbose_name='Total'
    )
    status = models.BooleanField(default=False)
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Data',
    )
    hour = models.TimeField(
        auto_now_add=True,
        verbose_name='Hora',
    )