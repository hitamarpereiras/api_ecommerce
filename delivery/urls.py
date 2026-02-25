from django.urls import path, include
from rest_framework.routers import DefaultRouter
from delivery.views import DeliveryManViewSet


router = DefaultRouter()
router.register(r'deliverymen', DeliveryManViewSet)

urlpatterns = [
    path('', include(router.urls)),
]