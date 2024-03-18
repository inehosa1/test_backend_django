from enum import Enum
from typing import List, Tuple


class AlertStatus(Enum):
    """
    Enum representing the status of an alert.

    Attributes:
        ACTIVE: The alert is active.
        EXPIRED: The alert has expired.
        PENDING: The alert is pending.
    """
    ACTIVE = 'ACTIVE'
    EXPIRED = 'EXPIRED'
    PENDING = 'PENDING'

    @classmethod
    def choices(cls) -> List[Tuple[str, str]]:
        """
        Get choices for the alert status.

        Returns:
            List[Tuple[str, str]]: List of tuples representing choices.
        """
        return [(key.value, key.name.capitalize()) for key in cls]