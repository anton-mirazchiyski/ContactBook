from django.urls import path

from contact_book.common.views import index

urlpatterns = [
    path('', index, name='index'),
]
