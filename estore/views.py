from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponse
from store.models import *
from .models import EbookModel


def ebookStore(request):
    category = request.GET.get('category')

    if category == None:
        products = EbookModel.objects.order_by('id')
    else:
        products = EbookModel.objects.filter(category=category)

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
    return render(request, 'estore/ebook.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response=HttpResponse(fh.read(), content_type="application/file")
            response['Content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
            return response

    raise Http404   

class EbookDetailView(DetailView):
    model = EbookModel
    template_name = 'estore/details.html'