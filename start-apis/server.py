from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^mm-24*i-6iecm7c@z9l+7%^ns^4g^z!8=dgffg4ulggr-4=1%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

SECRET_KEY = 'd3j@454545()(/)@zlck/6dsaf*#sdfsaf*#sadflj/6dsfk-11$)d6ixcvjsdfsdf&-u35#ayi'
DEV_VERSION = True

#INSTALLED_APPS += ['apis_highlighter', 'apis_bibsonomy']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': os.environ.get('APIS_DB_NAME'),
       'USER': os.environ.get('APIS_DB_USER'),
       'PASSWORD': os.environ.get('APIS_DB_PASSWORD'),
       'HOST': os.environ.get('APIS_DB_HOST', '127.0.0.1'),
       'PORT': os.environ.get('APIS_DB_PORT', '3306'),
   }
}


APIS_BIBSONOMY = {
    'url': 'https://www.bibsonomy.org/',
    'user': 'sennierer',
    'API key': '2dd4517aebd512152604fc4d84dc5133',
#    'group': 'histogis'
}


APIS_RELATIONS_FILTER_EXCLUDE += ['annotation', ]

