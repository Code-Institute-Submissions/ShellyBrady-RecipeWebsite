"""
Django settings for NiceAndEasyRecipes project.

Generated by 'django-admin startproject' using Django 3.2.18.

"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages
import dj_database_url
if os.path.isfile("env.py"):
    import env


BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

SECRET_KEY = os.environ.get('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["recipesite.herokuapp.com", "localhost", ]
X_FRAME_OPTIONS = 'SAMEORIGIN'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'django_summernote',
    'crispy_forms',
    "crispy_bootstrap5",
    'recipesite.apps.RecipesiteConfig',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = 'bootstrap5'


SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-info',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
    }


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NiceAndEasyRecipes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'NiceAndEasyRecipes.wsgi.application'


DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        ('django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'),
    },
    {
        'NAME':
        ('django.contrib.auth.password_validation.'
            'MinimumLengthValidator'),
    },
    {
        'NAME':
        ('django.contrib.auth.password_validation.'
            'CommonPasswordValidator'),
    },
    {
        'NAME':
        ('django.contrib.auth.password_validation.'
            'NumericPasswordValidator'),
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATICFILES_STORAGE = ('cloudinary_storage.storage.'
                       'StaticHashedCloudinaryStorage')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
