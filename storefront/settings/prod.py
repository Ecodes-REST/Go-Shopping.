import os
import dj_database_url
from .common import *

DEBUG= False

SECRET_KEY= os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['go-shopping-production.up.railway.app']


DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}


REDIS_URL= os.environ.get('REDIS_URL')

CELERY_BROKER_URL= REDIS_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 2525)


#HTTPS settings
SESSION_COOKIE_SECURE= True
CSRF_COOKIE_SECURE= True
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_TRUSTED_ORIGINS = ['https://go-shopping-production.up.railway.app']

