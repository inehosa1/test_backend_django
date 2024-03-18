from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from typing import Type, Any
from inventory.models import Product, Alert
from inventory.choices import AlertStatus


@receiver(post_save, sender=Product)
def create_alert(sender: Type[Product], instance: Product, created: bool, **kwargs: Any) -> None:
    """
    Signal handler to create an alert for a product nearing expiration.

    Args:
        sender (Type[Product]): The model class that sent the signal.
        instance (Product): The actual instance of the product being saved.
        created (bool): Indicates if the instance was created.
        kwargs: Additional keyword arguments.
    """
    if created:
        expiration_date = instance.expiration_date
        days_until_expiration = (expiration_date - timezone.now().date()).days
        status = AlertStatus.ACTIVE.value if days_until_expiration == 0 else AlertStatus.PENDING.value

        Alert.objects.create(
            product=instance,
            days_until_expiration=days_until_expiration,
            status=status
        )