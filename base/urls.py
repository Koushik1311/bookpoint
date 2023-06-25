from django.urls import path
from base.views import ContactView, AboutView
from . import views

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('', views.oldbookStore, name='home'),
]
