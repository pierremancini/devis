from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
with open('/etc/devis/django_secret_key.txt') as f:
    SECRET_KEY = f.read().strip()


ALLOWED_HOSTS = ['127.0.0.1', 'pierremancini.fr', '155.133.129.205']

STATIC_URL = '/gestion/static/'
STATIC_ROOT = '/var/www/devis/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'basic': {
            'format': '%(asctime)s %(name)-20s %(levelname)-8s %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'error.log'),
            'formatter': 'basic',
            'maxBytes': 1024*1024*15, # 15MB
            'backupCount': 10
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'INFO'
    },
}

try:
    from .local import *
except ImportError:
    pass
