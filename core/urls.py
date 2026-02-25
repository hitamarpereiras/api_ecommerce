from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('accounts.urls')),
    path('api/v1/', include('banners.urls')),
    path('api/v1/', include('customers.urls')),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('orders.urls')),
    path('api/v1/', include('delivery.urls')),
    path('api/v1/', include('sales.urls')),
    path('', admin.site.urls),
]
