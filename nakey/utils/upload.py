import imghdr
import random
import string


def get_random_name(length=25):
    y = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(25))
    return y


def banner_upload(instance, filename):
    """
    Returns location to saved into. Relative to MEDIA_ROOT folder in settings.
    Location format = <news> / <id> / <randomfilename>.
    """
    y = get_random_name()
    return 'banner/{}.{}'.format(y, imghdr.what(instance.image))


def item_upload(instance, filename):
    """
    Returns location to saved into. Relative to MEDIA_ROOT folder in settings.
    Location format = <news> / <id> / <randomfilename>.
    """
    y = get_random_name()
    return 'item/{}.{}'.format(y, imghdr.what(instance.image))
