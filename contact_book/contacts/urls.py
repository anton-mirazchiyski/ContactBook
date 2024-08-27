from django.urls import path, include

from contact_book.contacts.views import show_all_contacts, show_contacts_by_category, ContactCreateView, \
    ContactDetailView, ContactUpdateView, add_contact_email_or_address, search_contact, ContactDeleteView

urlpatterns = [
    path('all/', show_all_contacts, name='all_contacts'),
    path('<str:category>', show_contacts_by_category, name='family_contacts'),
    path('<str:category>', show_contacts_by_category, name='friends_contacts'),
    path('<str:category>', show_contacts_by_category, name='work_contacts'),
    path('<str:category>', show_contacts_by_category, name='other_contacts'),
    path('<int:pk>/', include([
        path('details/', ContactDetailView.as_view(), name='contact_details'),
        path('edit/', ContactUpdateView.as_view(), name='contact_edit'),
        path('additional_info/', add_contact_email_or_address, name='contact_additional_info'),
        path('delete/', ContactDeleteView.as_view(), name='contact_delete'),
    ])),
    path('search/', search_contact, name='contact_search'),
    path('create/', ContactCreateView.as_view(), name='contact_create'),
]
