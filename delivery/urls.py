from django.urls import path, include
from rest_framework.routers import DefaultRouter
from delivery.views import DeliveryManViewSet, RegisterView


router = DefaultRouter()
router.register(r'deliverys', DeliveryManViewSet)

urlpatterns = [
    path('deliverys/register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]