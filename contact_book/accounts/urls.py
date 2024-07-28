from django.urls import path, include

from contact_book.accounts.views import AccountCreateView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('create/', AccountCreateView.as_view(), name='account_create')
]
