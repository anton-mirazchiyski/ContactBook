from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from contact_book.contacts.forms import ContactCreateForm
from contact_book.contacts.models import Category, Contact
from contact_book.core.accounts_utils import get_current_account
from contact_book.core.mixins import CategoriesCreationMixin


def show_all_contacts(request):
    current_account = get_current_account(request)
    categories = Category.objects.all()

    context = {}
    for category in categories:
        name = str(category).lower() + '_contacts'
        contacts = current_account.contact_set.filter(category=category)
        context[name] = contacts

    return render(request, 'contacts/contacts-all.html', context)


def show_contacts_by_category(request, category):
    category = category.capitalize()
    current_account = get_current_account(request)
    contacts = current_account.contact_set.filter(category=category)

    context = {
        'contacts': contacts,
        'category': category,
        'number_of_contacts': contacts.count(),
    }

    return render(request, 'contacts/contacts-category.html', context)


class ContactCreateView(CategoriesCreationMixin, views.CreateView):
    model = Contact
    template_name = 'contacts/contact-create.html'
    form_class = ContactCreateForm
    success_url = reverse_lazy('all_contacts')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.account = self.request.user
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.check_for_categories_existence()
        return super().get(request, *args, **kwargs)
