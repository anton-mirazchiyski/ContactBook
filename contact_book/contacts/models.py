from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from contact_book.contacts.validators import validate_contact_name

UserModel = get_user_model()


class Contact(models.Model):
    MAX_LENGTH_NAME = 40
    MIN_LENGTH_NAME = 2
    min_length_error_message = 'Name must consist of at least 2 letters'

    MAX_LENGTH_NUMBER = 15

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=[MinLengthValidator(MIN_LENGTH_NAME, min_length_error_message), validate_contact_name],
        null=False, blank=False
    )

    phone_number = PhoneNumberField(
        region='BG',
        max_length=MAX_LENGTH_NUMBER,
        null=False, blank=False
    )

    email = models.EmailField(
        null=True, blank=True
    )

    account = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False, blank=True)

    def __str__(self):
        return f'{self.name} ({self.phone_number}) of user {self.account}'
