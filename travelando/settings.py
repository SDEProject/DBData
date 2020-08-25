"""
Django settings for travelando project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!%c(8yb!15_3!w5-s*3j3&973h0p8nt6c0(bhowsa#c+k_(m%n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mydb_data_layer',
    'drf_yasg',
    'rest_framework',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'travelando.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'travelando.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MYDB_HOST = 'localhost'
MYDB_PORT = 8000 if DEBUG else 80
SERVICE_MYDB_DATA_LAYER = "mydb_data_layer"

SERVICE_MYDB_ADAPTER_LAYER = "mydb_adapter_layer"
SERVICE_MYDB_ADAPTER_LAYER_PORT = 50005 if DEBUG else 80
SERVICE_MYDB_ADAPTER_LAYER_HOST = 'localhost'

SERVICE_CHOREOGRAPHER = 'choreographer'
SERVICE_CHOREOGRAPHER_PORT = 50006 if DEBUG else 80
SERVICE_CHOREOGRAPHER_HOST = 'localhost'

SERVICE_BUSINESS_LOGIC = 'business_search'
SERVICE_BUSINESS_LOGIC_PORT = 50007 if DEBUG else 80
SERVICE_BUSINESS_LOGIC_HOST = 'localhost'

SERVICE_PROCESS_CENTRIC = 'process_search'
SERVICE_PROCESS_CENTRIC_PORT = 50008 if DEBUG else 80
SERVICE_PROCESS_CENTRIC_HOST = 'localhost'

SERVICE_KNOWLEDGE = 'knowledge_graph'
SERVICE_KNOWLEDGE_PORT = 50009 if DEBUG else 80
SERVICE_KNOWLEDGE_HOST = 'localhost'

SERVICE_PROCESS_CENTRIC_DB = 'process_centric_db'
SERVICE_PROCESS_CENTRIC_DB_PORT = 50010 if DEBUG else 80
SERVICE_PROCESS_CENTRIC_DB_HOST = 'localhost'

SERVICE_BUSINESS_LOGIC_DB = 'business_logic_db_layer'
SERVICE_BUSINESS_LOGIC_DB_PORT = 50011 if DEBUG else 80
SERVICE_BUSINESS_LOGIC_DB_HOST = 'localhost'

SERVICE_QUERY_SELECTION = 'query_selection'
SERVICE_QUERY_SELECTION_PORT = 50012 if DEBUG else 80
SERVICE_QUERY_SELECTION_HOST = 'localhost'

SERVICE_NAME = os.environ.get('TRAVELANDO_SERVICE', "")
