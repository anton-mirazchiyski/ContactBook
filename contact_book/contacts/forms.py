from django import forms

from contact_book.contacts.models import Contact
from contact_book.core.mixins import FormControlMixin


class ContactBaseForm(FormControlMixin, forms.ModelForm):
    ADDRESS_FIELD_ROWS = 10
    ADDRESS_FIELD_COLUMNS = 25

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = {key: value for key, value in self.fields.items() if key != 'category'}
        self.apply_bootstrap_classes(fields)

    class Meta:
        model = Contact
        exclude = ['account']


class ContactCreateForm(ContactBaseForm):
    class Meta(ContactBaseForm.Meta):
        fields = ['name', 'phone_number', 'email', 'category']

        labels = {'email': 'Email (optional)'}

        widgets = {
            'name': forms.TextInput(attrs={'autofocus': True}),
            'category': forms.Select(attrs={'class': 'form-select border border-dark border-2'})
        }


class ContactEditForm(ContactBaseForm):
    class Meta(ContactBaseForm.Meta):
        widgets = {
            'address': forms.Textarea(attrs={
                'rows': ContactBaseForm.ADDRESS_FIELD_ROWS,
                'cols': ContactBaseForm.ADDRESS_FIELD_COLUMNS
            }),
            'category': forms.Select(attrs={'class': 'form-select border border-dark border-2'})
        }


class ContactEmailAndAddressForm(ContactBaseForm):
    class Meta(ContactBaseForm.Meta):
        fields = ['email', 'address']

        widgets = {
            'email': forms.EmailInput(attrs={'autofocus': True}),
            'address': forms.Textarea(attrs={
                'rows': ContactBaseForm.ADDRESS_FIELD_ROWS,
                'cols': ContactBaseForm.ADDRESS_FIELD_COLUMNS,
            })
        }
