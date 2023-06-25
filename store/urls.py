from django.urls import path
from . import views
from .views import CustomerCreationView, AddBookView, BookDetailView, BookUploadedView, BookEditView

urlpatterns = [
    path('oldstore/', views.oldbookStore, name="old_store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('search/', views.search, name="search"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

    path('customer/', CustomerCreationView.as_view(), name="customer"),
    path('add_product/', AddBookView.as_view(), name="add_product"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="book_detail"),
    path('uploaded/', BookUploadedView.as_view(), name="uploaded"),
    path('book_edit/<int:pk>', BookEditView.as_view(), name="book_edit"),
]