from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from contact_book.contacts.forms import ContactCreateForm, ContactEditForm, ContactEmailAndAddressForm, \
    ContactSearchForm, ContactDeleteForm
from contact_book.contacts.models import Category, Contact
from contact_book.core.accounts_utils import get_current_account
from contact_book.core.contacts_utils import find_searched_contacts
from contact_book.core.mixins import CategoriesCreationMixin


def show_all_contacts(request):
    current_account = get_current_account(request)
    categories = Category.objects.all()

    context = {'contacts': current_account.contact_set.all()}
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


def search_contact(request):
    searched_contacts = None

    if request.method == 'POST':
        search_form = ContactSearchForm(request.POST)
        if search_form.is_valid():
            contact_info = request.POST['search']
            searched_contacts = find_searched_contacts(request, contact_info)
            if not searched_contacts:
                messages.error(request, 'Contact does not exist or was not found')
            redirect('contact_search')

    search_form = ContactSearchForm()
    context = {
        'form': search_form,
        'searched_contacts': searched_contacts
    }

    return render(request, 'contacts/contact-search.html', context)


class ContactDeleteView(views.DeleteView):
    model = Contact
    template_name = 'contacts/contact-delete.html'
    success_url = reverse_lazy('all_contacts')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactDeleteForm(instance=self.object)
        return context
