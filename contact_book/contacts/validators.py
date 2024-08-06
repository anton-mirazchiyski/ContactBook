from django.core.exceptions import ValidationError


def validate_contact_name(value):
    for char in value:
        if not char.isalpha() and char != ' ':
            raise ValidationError('Please enter a valid name')
