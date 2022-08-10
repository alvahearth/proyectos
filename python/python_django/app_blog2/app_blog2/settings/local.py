from .base import *

ALLOWED_HOSTS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

