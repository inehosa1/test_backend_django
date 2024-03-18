from rest_framework.permissions import IsAuthenticated


class AuthorizationMixin:
    """
    Mixin to apply authentication conditionally to ModelViewSet.

    This class modifies the behavior of get_permissions to apply
    IsAuthenticated only if the condition specified in should_authenticate
    is met.
    """
    should_authenticate = lambda self, request: "docs" not in request.headers.get("Referer", "")

    def get_permissions(self):
        """
        Returns the list of permission classes for the current view.

        Applies IsAuthenticated if should_authenticate returns True, otherwise
        returns an empty list.
        """
        permission_classes = [IsAuthenticated] if self.should_authenticate(self.request) else []
        return [permission() for permission in permission_classes]