from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Order

User = get_user_model()


class OrderDetailTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user("alice", password="pw-alice")
        self.bob = User.objects.create_user("bob", password="pw-bob")
        self.order = Order.objects.create(customer=self.alice, subtotal=Decimal("50.00"))

    def test_owner_can_see_order(self):
        self.client.login(username="alice", password="pw-alice")
        response = self.client.get(reverse("order-detail", args=[self.order.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["total"], "54.90")

    def test_other_user_gets_404(self):
        self.client.login(username="bob", password="pw-bob")
        response = self.client.get(reverse("order-detail", args=[self.order.id]))
        self.assertEqual(response.status_code, 404)

    def test_anonymous_is_redirected_to_login(self):
        response = self.client.get(reverse("order-detail", args=[self.order.id]))
        self.assertEqual(response.status_code, 302)
