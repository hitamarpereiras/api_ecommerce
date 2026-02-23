from django.contrib import admin
from delivery.models import DeliveryMan

@admin.register(DeliveryMan)
class DeliveryManAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'phone',
        'vehicle_type',
        'account',
        'total_deliveries',
        'created_at',
    )

    list_filter = (
        'vehicle_type',
        'account',
        'created_at',
    )

    search_fields = (
        'user__username',
        'name',
        'phone',
        'cpf',
        'plate',
    )

    ordering = ('-created_at',)
