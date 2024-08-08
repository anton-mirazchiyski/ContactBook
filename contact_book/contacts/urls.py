from django.urls import path

from contact_book.contacts.views import show_all_contacts

urlpatterns = [
    path('all/', show_all_contacts, name='all_contacts'),
]
