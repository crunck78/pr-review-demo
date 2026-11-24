from decimal import Decimal

from django.conf import settings
from django.db import models


class Order(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders"
    )
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("4.90"))
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self) -> Decimal:
        return self.subtotal + self.shipping

    def __str__(self) -> str:
        return f"Order #{self.pk} ({self.customer})"
