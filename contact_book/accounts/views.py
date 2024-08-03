from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, resolve_url

from contact_book import settings
from contact_book.accounts.forms import AccountCreationForm, AccountLoginForm, AccountNamesSetupForm

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

    def get_success_url(self):
        if self.request.user.first_name != "":
            return resolve_url(settings.LOGIN_REDIRECT_URL)

        return resolve_url('names_setup')


def logout_account(request):
    logout(request)
    return redirect('login')


@login_required
def set_up_names(request):
    form = AccountNamesSetupForm()
    return render(request, 'accounts/account-names-setup.html', {'form': form})
