from django.contrib import admin
from products.models import Product

# Register your models here.
@admin.register(Product)
class ProdutAdmin(admin.ModelAdmin):
    list_display = [
        'id_account',
        'name',
        'category',
        'description',
        'price',
        'stock',
        'image_url',
        'created_at'
    ]
    list_filter = [
        'category',
        'created_at'
    ]