from django.test import TestCase
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.utils import timezone
from utils.functions import validate_future_date 


class ValidateFutureDateTestCase(TestCase):
    """
    Test case for validate_future_date function.
    """
    
    def test_future_date(self):
        """
        Test that a future date does not raise a ValidationError.
        """
        future_date = timezone.now().date() + timedelta(days=1)
        validate_future_date(future_date)  # No debe lanzar una excepción

    def test_past_date(self):
        """
        Test that a past date raises a ValidationError.
        """
        past_date = timezone.now().date() - timedelta(days=1)
        with self.assertRaises(ValidationError):
            validate_future_date(past_date)

    def test_current_date(self):
        """
        Test that the current date raises a ValidationError.
        """
        current_date = timezone.now().date()
        with self.assertRaises(ValidationError):
            validate_future_date(current_date)

    def test_datetime_instead_of_date(self):
        """
        Test that passing a datetime object raises a ValidationError.
        """
        now = timezone.now()
        with self.assertRaises(ValidationError):
            validate_future_date(now)