from datetime import datetime, date
from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_future_date(value) -> None:
    """
    Validate that the given date is in the future.

    Args:
        value: The date to validate, can be either datetime.date or datetime.datetime.
    """
    if isinstance(value, datetime):
        value = value.date()

    if not isinstance(value, date):
        raise ValidationError("Invalid date format.")

    if value <= timezone.now().date():
        raise ValidationError(f'{value}: Date must be in the future.')