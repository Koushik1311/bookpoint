import json
import datetime
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import CustomerForm, AddBookForm, BookEditForm
from .models import *


class CustomerCreationView(CreateView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('home')
    template_name = 'store/customer.html'

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Product.objects.filter(name__contains=searched)
        return render(request, 'store/search.html',
        {
            'searched':searched,
            'books':books
            })
    else:
        return render(request, 'store/search.html', {})
    

def oldbookStore(request):

    category = request.GET.get('category')

    if category == None:
        products = Product.objects.order_by('id')
    else:
        products = Product.objects.filter(category=category)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    # products = Product.objects.order_by('id')
    categories = Category.objects.all()
    context = {'products':products, 'cartItems':cartItems, 'categories':categories}
    return render(request, 'store/oldbook.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


class AddBookView(CreateView):
    model = Product
    form_class = AddBookForm
    template_name = 'store/add-product.html'
    success_url = reverse_lazy('home')


class BookDetailView(DetailView):
    model = Product
    template_name = 'store/bookdetail.html'


class BookUploadedView(ListView):
    model = Product
    template_name = 'store/uploaded.html'

class BookEditView(UpdateView):
    model = Product
    form_class = BookEditForm
    template_name = 'store/bookedit.html'
    success_url = reverse_lazy('uploaded')


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode'],
            )

    else:
        print("User is not logged in...")
    return JsonResponse('Payment complete...', safe=False)
