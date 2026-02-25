from django.contrib import admin
from products.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'description',
        'created_at',
        'updated_at'
    ]
    list_filter = [
        'name',
        'created_at'
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
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