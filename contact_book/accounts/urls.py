from django.urls import path, include

from contact_book.accounts.views import create_account, AccountLoginView

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('create/', create_account, name='account_create'),
]
