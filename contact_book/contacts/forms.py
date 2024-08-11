from django import forms

from contact_book.contacts.models import Contact
from contact_book.core.mixins import FormControlMixin


class ContactCreateForm(FormControlMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = {key: value for key, value in self.fields.items() if key != 'category'}
        self.apply_bootstrap_classes(fields)

    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email', 'category']

        widgets = {
            'category': forms.Select(attrs={'class': 'form-select border border-dark border-2'})
        }
