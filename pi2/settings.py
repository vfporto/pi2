import os
from decouple import config
from dj_database_url import parse as dburl


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECRET_KEY = '2xb2_7r&2=6*wrkg)zr101(g1brnpi=xbbrz+q0jm4qs!hy86&'
SECRET_KEY=config('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'pyzza.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pyzza.apps.PyzzaConfig',
    'rest_framework',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pi2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'pi2.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'pyzza',
#     }
# }
# DATABASES = {
#     'default': {
#         # 'ENGINE': 'django.db.backends.mysql',     #MySQL 1 -> pip install mysqlclient
#         # 'ENGINE': 'mysql.connector.django',       #MySQL 2 -> pip install mysql-connector-python==8.0.12
#         'ENGINE': 'django.db.backends.postgresql',  # Postgres-> pip install psycopg2
#         'NAME': 'pyzza',
#         'USER': 'postgres',  # Postgres
#         # 'USER': 'root',                           #MySQL
#         'PASSWORD': 'bancodedados',
#         'HOST': 'localhost',
#         'PORT': '5432',  # Porta Postgres: 5432  -  Porta MySQL: 3306
#
#         # Tentativa de resolver incompatibilidade das versoes > 8.0.12 do mysql-connector-python
#         # 'OPTIONS': {
#         #     'use_pure': True,
#         # }
#     }
# }
default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = { 'default': config('DATABASE_URL', default=default_dburl, cast=dburl), }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Configuracao para "django global static" files
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "staticfiles")
# ]

MEDIA_URL = '/imagens/'
MEDIA_ROOT = os.path.join(BASE_DIR, "imagens/")

# https://pyzza.herokuapp.com/ | https://git.heroku.com/pyzza.git
