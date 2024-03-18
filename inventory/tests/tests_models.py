from django.test import TestCase
from django.utils import timezone
from inventory.models import Product, Alert
from inventory.choices import AlertStatus


class ProductModelTestCase(TestCase):
    """
    Test case for the Product model.
    """

    def test_product_expiration_date_validation_future_date(self) -> None:
        """
        Test that creating a product with an expiration date in the future does not raise a ValidationError.
        """
        future_date = timezone.now().date() + timezone.timedelta(days=1)
        product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            stock_quantity=10,
            expiration_date=future_date
        )
        self.assertIsNotNone(product)


class AlertModelTestCase(TestCase):
    """
    Test case for the Alert model.
    """

    def test_alert_creation(self) -> None:
        """
        Test that an alert is created correctly.
        """
        product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            stock_quantity=10,
            expiration_date=timezone.now().date() + timezone.timedelta(days=1)
        )
        alert = Alert.objects.create(
            product=product,
            days_until_expiration=1,
            status=AlertStatus.PENDING.value
        )
        self.assertEqual(alert.product, product)
        self.assertEqual(alert.days_until_expiration, 1)
        self.assertEqual(alert.status, AlertStatus.PENDING.value)

    def test_alert_str_method(self) -> None:
        """
        Test the string representation of an alert.
        """
        product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            stock_quantity=10,
            expiration_date=timezone.now().date() + timezone.timedelta(days=1)
        )
        
        alert = Alert.objects.create(
            product=product,
            days_until_expiration=1,
            status=AlertStatus.PENDING.value
        )
        self.assertEqual(str(alert), f"Alert for {product} - 1 days before")