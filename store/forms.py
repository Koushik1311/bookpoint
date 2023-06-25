from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Customer, Product, Category
from useraccount.models import Account

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Product
        # model = Account
        fields = ('username', 'name', 'author', 'price','conditions',  'category', 'image', 'description')

        widgets = {
            'category': forms.Select(choices=choice_list, attrs = {"class": "form-control"})
        }


class BookEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('username', 'name', 'author', 'price','conditions',  'category', 'image', 'description')

        widgets = {
            'category': forms.Select(choices=choice_list, attrs = {"class": "form-control"})
        }