from django.core.exceptions import ObjectDoesNotExist

from contact_book.core.accounts_utils import get_current_account


def determine_contact_search_info(contact_info):
    is_name = True
    if '@' in contact_info:
        is_name = False
    return is_name


def find_searched_contacts(request, contact_info):
    searched_contacts = []
    current_account = get_current_account(request)

    is_name = determine_contact_search_info(contact_info)
    if is_name:
        searched_contacts = current_account.contact_set.filter(name__icontains=contact_info)
    else:
        try:
            searched_contact = (current_account.contact_set.
                                filter(email=contact_info).get())
            searched_contacts.append(searched_contact)
        except ObjectDoesNotExist:
            searched_contacts = None

    return searched_contacts
