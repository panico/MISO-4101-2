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

#desa
NAME_DB='dmbjrbf5tui1k'
USER_DB = 'czkxlkptpfljhy'
PWD_DB = 'UMq60bMuvQrXN0Ie9oJojMr5Yf'
HOST_DB = 'ec2-50-19-236-178.compute-1.amazonaws.com'

#test
#NAME_DB='d7rtbk4m2c6c3k'
#USER_DB = 'qpdmestgkkdxhn'
#PWD_DB = 'dHC9ClLm8wyX7vt6U6ZiEjzOlo'
#HOST_DB = 'ec2-50-17-181-147.compute-1.amazonaws.com'

#prod
#NAME_DB='dce330ch6019n5'
#USER_DB = 'jxkxkqtyokdkdf'
#PWD_DB = 'woo5BcTu62DbMZMvpRtf0KA7Li'
#HOST_DB = 'ec2-50-17-181-147.compute-1.amazonaws.com'


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

#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()
 
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
 
# Allow all host headers
ALLOWED_HOSTS = ['*']
 
# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
 
STATICFILES_DIRS = (
    #os.path.join(BASE_DIR, 'static'),
    os.path.join('core_app/', 'static'),
)


#Custome template folder
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
LOGIN_REDIRECT_URL='/'
LOGIN_URL='/login/'
