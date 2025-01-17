from django.contrib.auth.forms import BaseUserCreationForm, AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError

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

    first_name = forms.CharField(
        max_length=MAX_LEN_NAME,
        min_length=MIN_LEN_NAME,
        widget=forms.TextInput(attrs={'class': FormControlMixin.STYLE})
    )
    last_name = forms.CharField(
        max_length=MAX_LEN_NAME,
        min_length=MIN_LEN_NAME,
        widget=forms.TextInput(attrs={'class': FormControlMixin.STYLE})
    )

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not first_name.isalpha() or not last_name.isalpha():
            raise ValidationError('Name can contain only letters')

        return cleaned_data
