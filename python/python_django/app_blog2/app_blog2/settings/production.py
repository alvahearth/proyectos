from .base import *

ALLOWED_HOSTS = [
    'appblog2developer.herokuapp.com'
]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd1go5u9uvsi6c',
        'USER':  'jihhbpncvgcarb',
        'PASSWORD': '88e532a0efc8e6924efa4e3e96f9a892b7875a037908a68e9908d3f939c4e343',
        'HOST': 'ec2-100-24-139-146.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

