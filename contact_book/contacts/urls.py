from django.urls import path

from contact_book.contacts.views import show_all_contacts, show_contacts_by_category, ContactCreateView, \
    ContactDetailView, ContactUpdateView

urlpatterns = [
    path('all/', show_all_contacts, name='all_contacts'),
    path('<str:category>', show_contacts_by_category, name='family_contacts'),
    path('<str:category>', show_contacts_by_category, name='friends_contacts'),
    path('<str:category>', show_contacts_by_category, name='work_contacts'),
    path('<str:category>', show_contacts_by_category, name='other_contacts'),
    path('<int:pk>/details/', ContactDetailView.as_view(), name='contact_details'),
    path('<int:pk>/edit/', ContactUpdateView.as_view(), name='contact_edit'),
    path('create/', ContactCreateView.as_view(), name='contact_create'),
]
