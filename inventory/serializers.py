from rest_framework import serializers
from inventory.models import (
    Product, Alert
)
from inventory.choices import AlertStatus


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    Attributes:
        model (Product): The Product model to be serialized.
        fields (str): The fields to include in the serialization. Set to '__all__' to include all fields.
    """

    class Meta:
        model = Product
        fields = '__all__'
        
        
class AlertSerializer(serializers.ModelSerializer):
    """
    Serializer for the Alert model.
    """
    product = ProductSerializer()
    status = serializers.ChoiceField(
        choices=AlertStatus.choices(),
        error_messages={'invalid_choice': f"Invalid status value. Allowed values are: {', '.join([status.value for status in AlertStatus])}"}
    )

    class Meta:
        model = Alert
        fields = '__all__'