from django.urls import path, include

from contact_book.accounts.views import create_account, AccountLoginView, logout_account, set_up_names, \
    show_account_details, AccountDeleteView

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', logout_account, name='logout'),
    path('create/', create_account, name='account_create'),
    path('names/', set_up_names, name='names_setup'),
    path('<int:pk>/details/', show_account_details, name='account_details'),
    path('<int:pk>/delete/', AccountDeleteView.as_view(), name='account_delete'),
]
