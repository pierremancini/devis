from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
with open('/etc/devis/django_secret_key.txt') as f:
    SECRET_KEY = f.read().strip()


ALLOWED_HOSTS = ['127.0.0.1', 'pierremancini.fr', '155.133.129.205']

STATIC_URL = '/gestion/static/'
STATIC_ROOT = '/var/www/devis/static/'

try:
    from .local import *
except ImportError:
    pass
