from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, AlertViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'alerts', AlertViewSet)

app_name = 'inventory'

urlpatterns = [
    path('', include(router.urls)),
]