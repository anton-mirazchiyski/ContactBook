from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect
from django.views import generic as views

from contact_book.accounts.forms import AccountCreationForm

UserModel = get_user_model()


def create_account(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password1']
            user = UserModel.objects.create_user(username=username, email="", password=password)
            login(request, user)
            return redirect('all_contacts')

    form = AccountCreationForm()
    return render(request, 'accounts/account-create.html', {'form': form})
