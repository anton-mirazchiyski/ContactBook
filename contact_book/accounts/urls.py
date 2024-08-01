from django.urls import path, include

from contact_book.accounts.views import create_account, AccountLoginView, logout_account

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', logout_account, name='logout'),
    path('create/', create_account, name='account_create'),
]
