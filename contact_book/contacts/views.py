from django.shortcuts import render
from django.views import generic as views


class ShowAllContactsView(views.TemplateView):
    template_name = 'contacts/contacts-all.html'
