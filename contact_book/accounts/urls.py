from django.urls import path, include

from contact_book.accounts.views import create_account

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('create/', create_account, name='account_create')
]
