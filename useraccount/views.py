from multiprocessing.dummy import current_process
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import PasswordChangeView

from .forms import UserRegistraionForm, AccountAuthenticationForm, UserEditForm, PasswordChangeForm
from .models import Account


class SignUpView(CreateView):
    form_class = UserRegistraionForm
    get_success_url = '/customer'
    template_name = 'account/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.AllowAllUsersModelBackend')
        return HttpResponseRedirect(self.get_success_url)

def login_view(request, *args, **kwargs):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect("home")

        else:
            context['login_form'] = form

    return render(request, "account/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("home")

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get(next))
    return redirect


class ProfileView(DetailView):
    model = Account
    template_name = 'account/profile.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        current_user = get_object_or_404(Account, id=self.kwargs['pk'])
        context['current_user'] = current_user
        return context


class ProfileUpdateView(UpdateView):
    form_class = UserEditForm
    model = Account
    template_name = 'account/editprofile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'account/password-change.html'
    success_url = reverse_lazy('login')

