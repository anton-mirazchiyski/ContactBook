from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic as views

from contact_book.accounts.forms import AccountCreationForm

UserModel = get_user_model()


class AccountCreateView(views.CreateView):
    model = UserModel
    form_class = AccountCreationForm
    template_name = 'accounts/account-create.html'
