import re

from django.core.exceptions import ValidationError

MINIMUM_LENGTH = 8


def validate_minimum_length(value):
    if len(value) < MINIMUM_LENGTH:
        raise ValidationError("The password should be at least {0} characters long.".format(MINIMUM_LENGTH))


def validate_letters(value):

    # Number
    if not re.search(r'[0-9]', value):
        raise ValidationError("Password must contain at least 1 digit.")

    # Lowercase letters
    if not re.search(r'[a-z]', value):
        raise ValidationError("Password must contain at least 1 lowercase letter.")

    # Uppercase letters
    if not re.search(r'[A-Z]', value):
        raise ValidationError("Password must contain at least 1 uppercase letter.")

    # Special characters
    if not re.search(r'[!@#$%^&*+=]', value):
        raise ValidationError("Password must contain at least 1 special character.")
