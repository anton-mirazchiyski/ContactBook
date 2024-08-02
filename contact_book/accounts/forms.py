from django.contrib.auth.forms import BaseUserCreationForm, AuthenticationForm
from django import forms

from contact_book.core.mixins import FormControlMixin


class AccountCreationForm(FormControlMixin, BaseUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap_classes(self.fields)


class AccountLoginForm(FormControlMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap_classes(self.fields)


class AccountNamesSetupForm(FormControlMixin, forms.Form):
    MAX_LEN_NAME = 40
    MIN_LEN_NAME = 2

    first_name = forms.CharField(max_length=MAX_LEN_NAME, min_length=MIN_LEN_NAME)
    last_name = forms.CharField(max_length=MAX_LEN_NAME, min_length=MIN_LEN_NAME)

    form_fields = {'first_name': first_name, 'last_name': last_name}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap_classes(self.form_fields)
