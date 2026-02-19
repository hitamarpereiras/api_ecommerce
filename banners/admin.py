from django.contrib import admin
from banners.models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'banner_url', 
        'link', 
        'value_publi', 
        'status', 
        'created_at', 
        'updated_at'
    ]
    search_fields = [
        'name',
        'status'
    ]
