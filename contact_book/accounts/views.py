from django.contrib.auth import get_user_model
from django.contrib.auth.forms import BaseUserCreationForm
from django.shortcuts import render
from django.views import generic as views


UserModel = get_user_model()


class FormControlMixin:
    fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control border border-dark border-2'


class UserCreationForm(FormControlMixin, BaseUserCreationForm):
    fields = ('username', 'password1', 'password2')


class AccountCreateView(views.CreateView):
    model = UserModel
    form_class = UserCreationForm
    template_name = 'accounts/account-create.html'
