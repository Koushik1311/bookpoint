from operator import mod
from unicodedata import category
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from useraccount.models import Account

BOOK_CONDITION_CHOICES = (
    ('new', 'NEW'),
    ('good', 'GOOD'),
    ('fair', 'FAIR'),
    ('poor', 'POOR'),
)

# def user_img_directory_path(instance, filename):
#     return 'user_{0}/{1}'.format(instance.user.username, filename)


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.user)

class Product(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=250, null=True)
    category = models.CharField(max_length=200, default='Uncategorized')
    price = models.FloatField()
    digital = models.BooleanField(default=False)
    conditions = models.CharField(max_length=4, blank=False, null=False, choices=BOOK_CONDITION_CHOICES, default='good')
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.DecimalField(max_digits=7, decimal_places=2)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
