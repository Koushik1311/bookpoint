from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignUpView, ProfileView, ProfileUpdateView, PasswordChangeView
from .views import (
    login_view,
    logout_view,
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('edit_profile/', ProfileUpdateView.as_view(), name='edit-profile'),
    path('password/', PasswordChangeView.as_view(), name='change_password'),
]
