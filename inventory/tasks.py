from django.utils import timezone
from inventory.models import Alert
from inventory.choices import AlertStatus


def check_alerts() -> None:
    """
    Check and update the status of alerts based on the expiration date of associated products.

    This function iterates over all alerts and updates their status:
    - If the product's expiration date is today or within the next 5 days, the alert status is set to 'pending'.
    - If the product's expiration date is more than 5 days away, the alert status is set to 'active'.
    - If the product's expiration date has passed, the alert status is set to 'expired'.
    """
    alerts = Alert.objects.exclude(status=AlertStatus.EXPIRED.value)
    today = timezone.now().date()

    for alert in alerts:
        days_until_expiration = (alert.product.expiration_date - today).days
        if  (days_until_expiration > 0 and days_until_expiration <= 5):
            alert.status = AlertStatus.PENDING.value
        elif days_until_expiration > 5:
            alert.status = AlertStatus.ACTIVE.value
        elif days_until_expiration < 0:
            alert.status = AlertStatus.EXPIRED.value
        alert.save()