from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic as views

from contact_book.contacts.models import Category

UserModel = get_user_model()


def show_all_contacts(request):
    current_account = UserModel.objects.get(username=request.user.username)
    categories = Category.objects.all()

    context = {}
    for category in categories:
        name = str(category).lower() + '_contacts'
        contacts = current_account.contact_set.filter(category=category)
        context[name] = contacts

    return render(request, 'contacts/contacts-all.html', context)


def show_contacts_by_category(request, category):
    category = category.capitalize()
    current_account = UserModel.objects.get(username=request.user.username)
    contacts = current_account.contact_set.filter(category=category)

    context = {
        'contacts': contacts,
        'category': category,
        'number_of_contacts': contacts.count(),
    }

    return render(request, 'contacts/contacts-category.html', context)
