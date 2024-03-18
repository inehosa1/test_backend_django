from django.test import TestCase
from django.utils import timezone
from inventory.models import Product, Alert
from inventory.choices import AlertStatus
from inventory.tasks import check_alerts
from datetime import timedelta


class UtilsTestCase(TestCase):
    """
    Test case for the check_alerts function.
    """

    def setUp(self) -> None:
        """
        Create products with different expiration dates.
        """
        today = timezone.now().date()

        self.product_today = self.create_product(
            name='Product Today',
            description='Expires today',
            stock_quantity=10,
            expiration_date=today
        )

        self.product_future = self.create_product(
            name='Product Future',
            description='Expires in 3 days',
            stock_quantity=10,
            expiration_date=today + timedelta(days=3)
        )
        
        self.product_active = self.create_product(
            name='Product Active',
            description='Expires in 7 days',
            stock_quantity=10,
            expiration_date=today + timedelta(days=7)
        )
        
        self.product_expired = self.create_product(
            name='Product Expired',
            description='Expired 1 day ago',
            stock_quantity=10,
            expiration_date=today - timedelta(days=1)
        )

    def create_product(self, name, description, stock_quantity, expiration_date) -> None:
        """
        Create a product instance.
        """
        return Product.objects.create(
            name=name,
            description=description,
            stock_quantity=stock_quantity,
            expiration_date=expiration_date
        )

    def test_check_alerts(self) -> None:
        """
        Test that check_alerts updates the status of alerts correctly.
        """
        # Initial check to create alerts
        check_alerts()

        # Verify that alerts were created correctly
        self.assertEqual(Alert.objects.filter(status=AlertStatus.ACTIVE.value).count(), 2)
        self.assertEqual(Alert.objects.filter(status=AlertStatus.EXPIRED.value).count(), 1)

        # Update expiration dates to simulate time passing
        self.product_future.expiration_date = self.product_future.expiration_date - timedelta(days=1)
        self.product_future.save()
        self.product_active.expiration_date = self.product_active.expiration_date - timedelta(days=1)
        self.product_active.save()

        # Second check to update alerts
        check_alerts()

        # Verify that alerts were updated correctly
        self.assertEqual(Alert.objects.filter(status=AlertStatus.PENDING.value).count(), 1)
        self.assertEqual(Alert.objects.filter(status=AlertStatus.ACTIVE.value).count(), 2)
        self.assertEqual(Alert.objects.filter(status=AlertStatus.EXPIRED.value).count(), 1)