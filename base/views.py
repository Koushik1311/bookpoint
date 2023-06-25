import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.core.paginator import Paginator
from .forms import ContactForm
from .models import ContactModel
from store.models import *


# class HomeView(TemplateView):
#     template_name = 'home.html'


class ContactView(CreateView):
    model = ContactModel
    form_class = ContactForm
    template_name = 'contact.html'

class AboutView(TemplateView):
    template_name = 'about.html'

def oldbookStore(request):
    p = Paginator(Product.objects.all(), 4)
    page = request.GET.get('page')
    product_list = p.get_page(page)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    # current_time = datetime.datetime.now() 
    # start = current_time - datetime.timedelta(hours=167, minutes=59, seconds=59)
    products = Product.objects.order_by('id')
    context = {'products':products, 'product_list':product_list, 'cartItems':cartItems,}
    return render(request, 'home.html', context)
