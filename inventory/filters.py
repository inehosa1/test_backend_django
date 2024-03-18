from django_filters import rest_framework as filters
from inventory.models import Product, Alert
from inventory.choices import AlertStatus



class ProductFilter(filters.FilterSet):
    """
    Filter class for Product model.

    This filter allows filtering products based on their expiration date range.
    """

    min_expiration_date = filters.DateFilter(
        field_name='expiration_date', lookup_expr='gte'
    )
    max_expiration_date = filters.DateFilter(
        field_name='expiration_date', lookup_expr='lte'
    )

    class Meta:
        model = Product
        fields = ['min_expiration_date', 'max_expiration_date']
        
        

class AlertFilter(filters.FilterSet):
    """
    Filter class for Alert model.

    This filter allows filtering alerts based on their status.
    """

    min_days_until_expiration = filters.NumberFilter(
        field_name='days_until_expiration', lookup_expr='gte'
    )
    
    max_days_until_expiration = filters.NumberFilter(
        field_name='days_until_expiration', lookup_expr='lte'
    )
    
    def filter_status(self, queryset: Alert, name: str, value: AlertStatus) -> Alert:
        """
        Filter the queryset by alert status.

        Args:
            queryset (Alert): The instance to filter.
            name (str): The name of the field to filter on.
            value (AlertStatus): The value of the alert status to filter by.

        Returns:
            QuerySet: The filtered queryset.
        """
        return queryset.filter(status=value)

    class Meta:
        model = Alert
        fields = ['status', 'min_days_until_expiration', 'max_days_until_expiration']