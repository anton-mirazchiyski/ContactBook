from django.contrib.auth.forms import BaseUserCreationForm, AuthenticationForm

from contact_book.core.mixins import FormControlMixin


class AccountCreationForm(FormControlMixin, BaseUserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap_classes(self.fields)


class AccountLoginForm(FormControlMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap_classes(self.fields)
