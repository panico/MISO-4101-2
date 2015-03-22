"""
Django settings for MySmartHome project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v&g1yt))+lxc0cge$-o0urwbts9snzd@2)fb0e-k8(&w=%llwg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'django_extensions',
    'core_app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'MySmartHome.urls'

WSGI_APPLICATION = 'MySmartHome.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#NAME_DB='mySmartHome'
#USER_DB = 'postgres'
#PWD_DB = '000000'
#HOST_DB = 'localhost'

NAME_DB='dmbjrbf5tui1k'
USER_DB = 'czkxlkptpfljhy'
PWD_DB = 'UMq60bMuvQrXN0Ie9oJojMr5Yf'
HOST_DB = 'ec2-50-19-236-178.compute-1.amazonaws.com'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': NAME_DB,
        'USER': USER_DB,
        'PASSWORD': PWD_DB,
        'HOST': HOST_DB,
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

#Custome template folder

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
LOGIN_REDIRECT_URL='/'
LOGIN_URL='/login/'
