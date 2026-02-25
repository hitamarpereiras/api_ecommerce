from django.contrib import admin
from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'phone',
        'address',
        'house_number',
        'coins',
        'avatar_url',
        'created_at',
        'updated_at',
    ]
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'phone', 'address']
