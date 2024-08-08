from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views import generic as views

UserModel = get_user_model()


def show_all_contacts(request):
    current_account = UserModel.objects.get(username=request.user.username)
    contacts = current_account.contact_set.all()

    context = {'contacts': contacts}

    return render(request, 'contacts/contacts-all.html', context)
