# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
# from store.views import ebookStore, oldbookStore, cart, checkout, updateItem, processOrder, CustomerCreationView


# class TestUrls(SimpleTestCase):
#     def test_ebookstore_url_resolves(self):
#         url = reverse('ebook')
#         self.assertEquals(resolve(url).func, ebookStore)

#     def test_oldbookstore_url_resolves(self):
#         url = reverse('old_book')
#         self.assertEquals(resolve(url).func, oldbookStore)

#     def test_cart_url_resolves(self):
#         url = reverse('cart')
#         self.assertEquals(resolve(url).func, cart)

#     def test_checkout_url_resolves(self):
#         url = reverse('checkout')
#         self.assertEquals(resolve(url).func, checkout)

#     def test_update_url_resolves(self):
#         url = reverse('update_item')
#         self.assertEquals(resolve(url).func, updateItem)

#     def test_processorder_url_resolves(self):
#         url = reverse('process_order')
#         self.assertEquals(resolve(url).func, processOrder)

#     def test_customercreate_url_resolves(self):
#         url = reverse('customer')
#         self.assertEquals(resolve(url).func.view_class, CustomerCreationView)
