from django.contrib.auth import get_user_model
from django.shortcuts import render

from contact_book.core.accounts_utils import get_current_account

UserModel = get_user_model()


def index(request):
    all_contacts = []
    try:
        current_account = get_current_account(request)
        all_contacts = current_account.contact_set.all()
    except UserModel.DoesNotExist:
        current_account = None

    context = {
        'total_number_of_contacts': len(all_contacts),
    }

    return render(request, 'common/index.html', context)
