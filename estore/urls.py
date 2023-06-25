from django.urls import path
from . import views
from .views import EbookDetailView

urlpatterns = [
    path('estore/', views.ebookStore, name="estore"),
    path('ebook/<int:pk>/', EbookDetailView.as_view(), name="ebook_detail"),
]