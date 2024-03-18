from django_filters import rest_framework as django_filters
from utils.base_model_view_set import BaseModelViewSet
from inventory.models import Product, Alert
from inventory.serializers import ProductSerializer, AlertSerializer
from inventory.filters import ProductFilter, AlertFilter


class ProductViewSet(BaseModelViewSet):
    """
    ViewSet for the Product model.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_class = ProductFilter
    

class AlertViewSet(BaseModelViewSet):
    """
    ViewSet for the Alert model.
    """
    queryset = Alert.objects.select_related("product").all()
    serializer_class = AlertSerializer
    http_method_names = ['get']
    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_class = AlertFilter