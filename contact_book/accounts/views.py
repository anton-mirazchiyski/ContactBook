from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse_lazy
from django.views import generic as views

from contact_book import settings
from contact_book.accounts.forms import AccountCreationForm, AccountLoginForm, AccountNamesSetupForm
from contact_book.core.accounts_utils import get_current_account

UserModel = get_user_model()


def create_account(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password1']
            user = UserModel.objects.create_user(username=username, email="", password=password)
            login(request, user)
            return redirect('names_setup')

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
    if request.method == 'POST':
        form = AccountNamesSetupForm(request.POST)
        if form.is_valid():
            user = UserModel.objects.get(username=request.user.username)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            return redirect('all_contacts')

    form = AccountNamesSetupForm()
    return render(request, 'accounts/account-names-setup.html', {'form': form})


@login_required
def show_account_details(request, pk):
    current_account = get_current_account(request)
    context = {'account': current_account}
    return render(request, 'accounts/account-details.html', context)


class AccountDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/account-delete.html'
    success_url = reverse_lazy('index')
