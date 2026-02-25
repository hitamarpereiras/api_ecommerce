from django.contrib import admin
from sales.models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'total',
        'subtotal',
        'remaining',
        'payment_method',
        'rate_delivery',
        'account',
        'order',
        'status',
        'collaborator',
        'observation'
    )
    list_filter = ('status',)
    search_fields = ('account__name', 'order__id')
