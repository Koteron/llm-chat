import os

from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET", default='django-insecure-(whfk+d(bm%ep56&xs-w+lgd7t-fqoa0z86n6mpzs0_w=a^0qw')

DEBUG = os.getenv("DJANGO_DEBUG", default=1)

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", default="127.0.0.1,localhost").split(",")

INSTALLED_APPS = [
    'llmchat.apps.MongoAdminConfig',
    'llmchat.apps.MongoAuthConfig',
    'llmchat.apps.MongoContentTypesConfig',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mongodb_backend',
    
    'llama_api.apps.LlamaApiConfig',
    "rest_framework",
    "djoser",
    "drf_spectacular",
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

ROOT_URLCONF = 'llmchat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'llmchat.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_backend',
        'HOST': 'mongodb://' + os.getenv("MONGO_HOST", default="localhost") +
          ':' + os.getenv("MONGO_PORT", default="27017") + '/',
        'NAME': os.getenv("MONGO_DB_NAME", default="llmchat"),
        'USER': os.getenv("MONGO_USER", default="llm_user"),
        'PASSWORD': os.getenv("MONGO_PASSWORD", default="supersecret"),
    },
}

DATABASE_ROUTERS = ["django_mongodb_backend.routers.MongoRouter"]

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MIGRATION_MODULES = {
    'admin': 'mongo_migrations.admin',
    'auth': 'mongo_migrations.auth',
    'contenttypes': 'mongo_migrations.contenttypes',
}

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

DJOSER = {
    "LOGIN_FIELD": "username",
    "LOGOUT_ON_PASSWORD_CHANGE": True,
    'SERIALIZERS': {
        'user_create': 'llama_api.serializers.CustomUserCreateSerializer',
        'user': 'llama_api.serializers.CustomUserSerializer',
    },
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}


SPECTACULAR_SETTINGS = {
    "TITLE": "LLM Chat API",
    "DESCRIPTION": "Django REST API for LLaMA chat with JWT auth",
    "VERSION": "1.0.0",

    "SERVE_AUTHENTICATION": ["rest_framework_simplejwt.authentication.JWTAuthentication"],

    "SECURITY": [
        {
            "bearerAuth": [],
        }
    ],

    "COMPONENT_SPLIT_REQUEST": True,
}

