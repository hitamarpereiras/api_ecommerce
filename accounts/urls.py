from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import AccountViewSet
from accounts.views import RegisterView

router = DefaultRouter()
router.register('accounts', AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]