from .base import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
# with open('/etc/devis/django_secret_key.txt') as f:
#     SECRET_KEY = f.read().strip()
SECRET_KEY = "azrrgeràç'tuéibàngrezoiçph8967/*&eé%%"

ALLOWED_HOSTS = ['localhost', '*']

INTERNAL_IPS = [
    '127.0.0.1'
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS += [
    'debug_toolbar'
]

STATIC_URL = '/static/'

try:
    from .local import *
except ImportError:
    pass
