"""
Django settings for pi2 project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2xb2_7r&2=6*wrkg)zr101(g1brnpi=xbbrz+q0jm4qs!hy86&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'pyzza.apps.PyzzaConfig',
    'pyzza',
    'rest_framework',
    'bebidas',
    'pizzas',
    'pessoas',
    'pedidos',
    'site_interno',
    # 'django_filters',
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
#         'NAME': os.path.join(BASE_DIR, "db.sqlite3"),
#     }
# }

DATABASES = {
    # Mudar para default o banco que quiser usar, e
    'default': {
    # 'sqlite'{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "db.sqlite3"),
    },

    'POSTGRES': { #Postgres
        'ENGINE': 'django.db.backends.postgresql',  #Postgres-> pip install psycopg2
        'NAME': 'pyzza',
        'USER': 'postgres',
        'PASSWORD': 'bancodedados',
        'HOST': 'localhost',
        'PORT': '5432',
    },

    'mysql': {  # MySQL
        # 'ENGINE': 'django.db.backends.mysql',     #MySQL 1 -> pip install mysqlclient
        'ENGINE': 'mysql.connector.django',       #MySQL 2 -> pip install mysql-connector-python==8.0.12
        'NAME': 'pyzza',
        'USER': 'root',
        'PASSWORD': 'bancodedados',
        'HOST': 'localhost',
        'PORT': '3306',
        # Tentativa de resolver incompatibilidade das versoes > 8.0.12 do mysql-connector-python
        # 'OPTIONS': {
        #     'use_pure': True,
        # }
    },
}

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# Configuracao para "django global static" files
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "staticfiles")
# ]

MEDIA_URL = '/imagens/'
MEDIA_ROOT = os.path.join(BASE_DIR, "imagens/")

SUIT_CONFIG={
    # header
    'ADMIN_NAME': 'Pyzzarella',
    'HEADER_DATE_FORMAT': 'l, j \d\e F \d\e Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    # ),

    # misc
    # 'LIST_PER_PAGE': 15

    'MENU_ICONS': {
        'pedidos': 'icon-shopping-cart',
        'bebidas': 'icon-glass',
        'auth': 'icon-lock',
        'pessoas': 'icon-user',
        'pizzas': 'icon-inbox',
    },
'MENU': (
        'sites',
            {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
        '-',
        {'label':'Pessoas', 'icon':'icon-user', 'models': ('pessoas.Cliente', 'pessoas.Entregador'),
            # 'permissions': 'empresa.view_empresa'
        },
        {
            'app': 'pizzas',
            'label': 'Pizzas',
            'icon': 'icon-inbox',
            'models': ('TamanhoPizza','TipoPizza', 'SaborBorda','SaborPizza','Ingrediente'),
            # 'permissions': 'empresa.view_empresa'
        },
        {
            'label': 'Bebidas',
            'icon': 'icon-glass',
            'models': ('bebidas.Bebida', 'bebidas.TamanhoBebida'),
            # 'permissions': 'empresa.view_empresa'
        },
        {
            'label': 'Pedidos',
            'icon': 'icon-shopping-cart',
            'models': (
                'pedidos.Pedido', 'pedidos.FormaDePagamento'),
            # 'permissions': 'empresa.view_empresa'
        },
        '-',
        {
            'label': 'Relatórios',
            'icon':'icon-list-alt',
            'url': '/interno/',
            # 'permissions': 'empresa.view_empresa'
        },
        { 'label': 'Relatório de Ingredientes', 'icon': 'icon-list-alt', 'url': '/interno/rel_ingredientes/',},

),

}
# Lista de icones utilizaveis
# https://deniskrumko.github.io/django-suit-icons/


# https://django-suit.readthedocs.io/en/latest/configuration.html
# # Rename app and set icon
# {'app': 'auth', 'label': 'Authorization', 'icon': 'icon-lock'},
#
# # Reorder app models
# {'app': 'auth', 'models': ('user', 'group')},
#
# # Custom app, with models
# {'label': 'Settings', 'icon': 'icon-cog', 'models': ('auth.user', 'auth.group')},
#
# # Cross-linked models with custom name; Hide default icon
# {'label': 'Custom', 'icon': None, 'models': (
#     'auth.group',
#     {'model': 'auth.user', 'label': 'Staff'}
# )},
#
# # Custom app, no models (child links)
# {'label': 'Users', 'url': 'auth.user', 'icon': 'icon-user'},
#
# # Separator
# '-',
#
# # Custom app and model with permissions
# {'label': 'Secure', 'permissions': 'auth.add_user', 'models': [
#     {'label': 'custom-child', 'permissions': ('auth.add_user', 'auth.add_group')}
# ]},