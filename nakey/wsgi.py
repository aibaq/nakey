import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nakey.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'BaseConfiguration')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
