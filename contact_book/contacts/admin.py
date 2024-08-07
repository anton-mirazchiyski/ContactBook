from django.contrib import admin

from contact_book.contacts.models import Contact, Category

admin.site.register(Category)
admin.site.register(Contact)
