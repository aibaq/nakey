from django.conf import settings
from urllib.parse import urljoin


def get_full_url(image):
    try:
        if not image:
            return None
        return urljoin(settings.SITE_URL, image.url)
    except Exception as e:
        print(str(e))
        return None
