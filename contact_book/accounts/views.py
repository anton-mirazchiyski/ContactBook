from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from contact_book.accounts.forms import AccountCreationForm, AccountLoginForm

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


class AccountLoginView(LoginView):
    template_name = 'accounts/account-login.html'
    authentication_form = AccountLoginForm
    next_page = 'all_contacts'


def logout_account(request):
    logout(request)
    return redirect('login')
