"""
Django settings for Healthmap project.

Generated by 'django-admin startproject' using Django 4.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-do*1m5m((oltg0(_4)u&+wjcm1^8@8!j^07*2_7x(pt)5acqf8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'https://healthmap.onrender.com', 'healthmap.onrender.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.gis',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'hospitals',
    'leaflet',
    'mapwidgets',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Healthmap.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'Healthmap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'Healthmap',
#         'USER': 'postgres',
#         'PASSWORD': 'marvade',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


import os
import dj_database_url

DATABASE_URL = os.getenv('DATABASE_URL')
print(f"Using DATABASE_URL: {DATABASE_URL}")
DATABASES = {
    'default': dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,  # Optional: Adjust connection pooling
        ssl_require=True   # Optional: If you need SSL for connections
    )
}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# if os.getenv('RENDER'):
#     DATABASE_URL = os.getenv('DATABASE_URL')
#     print(f"Using DATABASE_URL: {DATABASE_URL}")
#     DATABASES = {
#         'default': dj_database_url.config(
#             default=DATABASE_URL,
#             conn_max_age=600,  # Optional: Adjust connection pooling
#             ssl_require=True   # Optional: If you need SSL for connections
#         )
#     }
#     DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'  # Ensure PostGIS is set
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.contrib.gis.db.backends.postgis',
#             'NAME': 'Healthmap',
#             'USER': 'postgres',
#             'PASSWORD': 'marvade',
#             'HOST': 'localhost',
#             'PORT': '5432',
#         }
#     }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = '/static/'

# #STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (7.2571, 5.1951),  # Default center (Akure)
    'DEFAULT_ZOOM': 13,  # Default zoom level
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 20,
    'TILES': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    'ATTRIBUTION_PREFIX': 'Powered by Akure Hospitals',
}

# # Set GDAL and GEOS library paths
# GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\gdal309.dll'  # Replace XXX with the version number
# GEOS_LIBRARY_PATH = r'C:\OSGeo4W\bin\geos_c.dll'

# import platform

# # Detect if running on Windows or Linux
# if platform.system() == 'Windows':
#     # Local development (Windows)
#     GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\gdal309.dll'
#     GEOS_LIBRARY_PATH = r'C:\OSGeo4W\bin\geos_c.dll'
# else:
#     # Production (Linux on Render)
#     GDAL_LIBRARY_PATH = '/usr/lib/libgdal.so'  # Path to GDAL library on Linux
#     GEOS_LIBRARY_PATH = '/usr/lib/libgeos_c.so'  # Path to GEOS library on Linux


# # GDAL Library Path (detected from environment or fallback)
# GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH', '/usr/lib/libgdal.so')

# import os

# GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH')

# if GDAL_LIBRARY_PATH is None:
#     raise Exception("GDAL library path is not set!")

import os
GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH')