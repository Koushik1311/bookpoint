from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from store.models import Customer, Product, Order, OrderItem, ShippingAddress
import json


class TestView(TestCase):
    def setUp(self):
        self.clint = Client()
        self.eproduct_url = reverse('ebook')
        self.phyproduct_url = reverse('old_book')
        self.cart_url = reverse('cart')
        self.checkout_url = reverse('cart')

    def test_ebooklist_list_GET(self):
        response = self.client.get(self.eproduct_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/ebook.html')

    def test_oldbooklist_list_GET(self):
        response = self.client.get(self.phyproduct_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/oldbook.html')

    def test_cart_list_GET(self):
        response = self.client.get(self.cart_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/cart.html')

    def test_checkout_list_GET(self):
        response = self.client.get(self.checkout_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/checkout.html')
