from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Account


class UserRegistraionForm(UserCreationForm):
    email = forms.EmailField(max_length=60,)


    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')


class UserEditForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'gender', 'birthday')


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("email", "password")

        def __init__(self, *args, **kwargs):
            self.request = kwargs.pop('request', None)
            super(AccountAuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")


class PasswordChangeForm(PasswordChangeForm):

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

