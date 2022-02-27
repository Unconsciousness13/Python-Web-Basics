from django.core.exceptions import ValidationError

VALIDATE_ONLY_LETTERS_NUMS_UNDER_EXCEPTION_MESSAGE = 'Ensure this value contains only letters, numbers, and underscore.'


def validate_only_letters_nums_underscore(value):
    if not all(c.isalnum() or c == '_' for c in value):
        raise ValidationError(VALIDATE_ONLY_LETTERS_NUMS_UNDER_EXCEPTION_MESSAGE)


# def validate_only_letters_nums_underscore(value):
#     if not value.isalnum() or not '':
#         raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')