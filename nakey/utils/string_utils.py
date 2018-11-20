from django.core.validators import validate_email
import phonenumbers


def valid_phone(phone):
    try:
        phone_object = phonenumbers.parse(phone, None)
        if not phonenumbers.is_valid_number(phone_object):
            return False
        return True
    except:
        return False


def valid_email(email):
    try:
        validate_email(email)
        return True
    except:
        return False


def price_to_int(value):
    """
    E.g. value="4,3 млн тг" -> 4300000 тг
    """
    return int(float(value.strip().split()[0].replace(",", ".")) * (10**6))
