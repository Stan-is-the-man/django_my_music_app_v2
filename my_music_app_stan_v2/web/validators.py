from django.core.exceptions import ValidationError


def validate_only_letters_numbers_underscore(value):
    
    for char in value:
        if not char.isalnum() and char != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
