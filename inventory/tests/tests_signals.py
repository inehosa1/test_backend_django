from django.test import TestCase
from django.utils import timezone
from inventory.models import Product
from inventory.choices import AlertStatus
from django.db.models.signals import post_save
from django.test import override_settings
from unittest.mock import patch


class SignalTestCase(TestCase):
    """
    Test case for the post_save signal.
    """

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_create_alert_signal(self) -> None:
        """
        Test that the create_alert signal creates an alert for a product nearing expiration.
        """
        # Create a product with an expiration date 1 day from now
        expiration_date = timezone.now().date() + timezone.timedelta(days=1)
        product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            stock_quantity=10,
            expiration_date=expiration_date
        )

        # Emulate the signal being sent
        with patch('inventory.signals.Alert.objects.create') as mock_create:
            post_save.send(sender=Product, instance=product, created=True)

            # Verify that an alert is created with the correct status
            days_until_expiration = (expiration_date - timezone.now().date()).days
            expected_status = AlertStatus.ACTIVE.value if days_until_expiration == 0 else AlertStatus.PENDING.value
            mock_create.assert_called_once_with(
                product=product,
                days_until_expiration=days_until_expiration,
                status=expected_status
            )