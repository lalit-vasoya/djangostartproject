from django.core.exceptions import ValidationError


def validate_the_author_email(value):
    if not "lalit" in value:
        raise ValidationError("Author Email Not Valid")
    return value
    
