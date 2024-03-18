from django.db import models
from inventory.choices import AlertStatus
from utils.functions import validate_future_date


class Product(models.Model):
    """
    A model representing a product in the inventory.

    Attributes:
        name (str): The name of the product.
        description (str): The description of the product.
        stock_quantity (int): The quantity of the product in stock.
        expiration_date (date): The expiration date of the product.
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    stock_quantity = models.IntegerField()
    expiration_date = models.DateField(validators=[validate_future_date])
    
    def __str__(self) -> str:
        return self.name
    

class Alert(models.Model):
    """
    Model to store alerts for products nearing expiration.

    Attributes:
        product (Product): The product associated with the alert.
        days_until_expiration (int): The number of days until the product expires.
        created_at (datetime): The timestamp when the alert was created.
        status (str): The status of the alert (active, expired, pending).
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    days_until_expiration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=AlertStatus.choices(),
        default=AlertStatus.PENDING.value
    )

    def __str__(self) -> str:
        return f"Alert for {self.product} - {self.days_until_expiration} days before"