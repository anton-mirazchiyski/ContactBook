from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from contact_book.contacts.forms import ContactCreateForm, ContactEditForm, ContactEmailAndAddressForm, \
    ContactSearchForm
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


class ContactDetailView(views.DetailView):
    model = Contact
    template_name = 'contacts/contact-details.html'


class ContactUpdateView(views.UpdateView):
    model = Contact
    template_name = 'contacts/contact-edit.html'
    form_class = ContactEditForm
    success_url = reverse_lazy('all_contacts')


def add_contact_email_or_address(request, pk):
    current_account = get_current_account(request)
    contact = current_account.contact_set.filter(pk=pk).get()

    if request.method == 'POST':
        form = ContactEmailAndAddressForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_details', pk)
    form = ContactEmailAndAddressForm(instance=contact)

    context = {
        'form': form,
        'contact': contact
    }

    return render(request, 'contacts/contact-email-and-address.html', context)


def determine_contact_info(contact_info):
    is_name = True
    if '@' in contact_info:
        is_name = False
    return is_name


def search_contact(request):
    current_account = get_current_account(request)
    searched_contact = None

    if request.method == 'POST':
        search_form = ContactSearchForm(request.POST)
        if search_form.is_valid():
            contact_info = request.POST['search']
            is_name = determine_contact_info(contact_info)
            try:
                if is_name:
                    searched_contact = (current_account.contact_set.
                                        filter(name__icontains=contact_info).get())
                else:
                    searched_contact = (current_account.contact_set.
                                        filter(email__contains=contact_info).get())
            except ObjectDoesNotExist:
                searched_contact = None
            redirect('contact_search')

    search_form = ContactSearchForm()
    context = {
        'form': search_form,
        'contact': searched_contact
    }

    return render(request, 'contacts/contact-search.html', context)
