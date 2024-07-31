from django.urls import path

from contact_book.contacts.views import ShowAllContactsView

urlpatterns = [
    path('all/', ShowAllContactsView.as_view(), name='all_contacts'),
]
