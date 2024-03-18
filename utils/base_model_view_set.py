from rest_framework import viewsets
from utils.mixin import AuthorizationMixin


class BaseModelViewSet(AuthorizationMixin, viewsets.ModelViewSet):
    pass