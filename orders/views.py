from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET

from .models import Order


def serialize_order(order: Order) -> dict:
    return {
        "id": order.id,
        "subtotal": str(order.subtotal),
        "shipping": str(order.shipping),
        "total": str(order.total),
    }


@login_required
@require_GET
def order_detail(request, order_id: int):
    # Customers may only see their own orders.
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    return JsonResponse(serialize_order(order))
