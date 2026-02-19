from django.contrib import admin
from accounts.models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'phone', 
        'address', 
        'cnpj', 
        'avatar_url', 
        'instagram_url', 
        'facebook_url', 
        'other_url', 
        'created_at', 
        'updated_at'
    ]
    search_fields = [
        'name',
        'cnpj',
        'phone'
    ]
