from django.contrib import admin
from inventory.models import Product, Alert


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    pass