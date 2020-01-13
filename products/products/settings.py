import os
import logging
from decouple import config, Csv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = config('SECRET_KEY')


DEBUG = config('DEBUG', default=False, cast=bool)


ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'django_events_sourcing',
    'apps.api',
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


ROOT_URLCONF = 'products.urls'


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


WSGI_APPLICATION = 'products.wsgi.application'


DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('NAME_PSQL'),
            'USER': config('USER_PSQL'),
            'PASSWORD': config('PASSWORD_PSQL'),
            'HOST': config('HOST_PSQL', default='localhost'),
            'PORT': config('PORT_PSQL', default='5432')
        }
}


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_deploy')


## REST_FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination'
}

## Nameko
# Config to be passed to ClusterRpcProxy
SERVICE_NAME = 'products'
NAMEKO_CONFIG = {
    'AMQP_URI': config('AMQP_URI',
                       default='amqp://guest:guest@localhost:5672/')
}
DJANGO_NAMEKO_STANDALONE_APPS = ('apps.api', )

# List of Model and Serializer to be used for the event.

MODELS_CRUD_EVENT = [
    {'model': 'api.Product'}
]
"""
Usage:
 
Suppose a model: 

class ModelWithStatus(models.Model):
  STATUS_CHOICES = (('started', 'Started'), ('finished', 'Finished'))
  status = models.CharField(max_lenght=200, choices=STATUS_CHOICES)

Then we have: 

MODELS_CRUD_EVENT = 
[
    {'model': app.ModelWithStatus', 
     'serializer': 'app.serializers.ModelWithStatusSerializer',
     'status_field': 'status'},
]

The only required key is model, the others are optional.
 . serializer: It's the serializer that will be used to dispatch the data. 
               If no serializer is given, a ModelSerializer with all fields is used.
               
 . status_field: It's the field which we are going to use as the events name 
                 (Usually a CharField with choices).
                 Notes:
                 if no field is given, the events are: model_name__created, 
                 model_name__updated, model_name__deleted.
                 If the field is given then the events are: model_name__[status]
"""


LOG_LEVEL = config('LOG_LEVEL', default='INFO', cast=str)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # How to format the output
    'formatters': {
        'standard': {
            'format':
            "[%(asctime)s] %(threadName)s, %(name)s, %(levelname)s [%(filename)s:%(lineno)d]:  %(message)s",
            'datefmt':
            "%d/%m/%Y %H:%M:%S"
        },
        'djangolog': {
            'format':
            '[%(asctime)s] - %(name)s, [%(filename)s:%(lineno)d]: %(message)s',
            'datefmt':
            '%d/%m/%Y %H:%M:%S'
        },
    },
    # Log handlers (where to go)
    'handlers': {
        'console': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'log_file': {
            'level': LOG_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + '/log/django_app.log',
            'maxBytes': (1024 * 1024) * 2,
            'backupCount': 10,
            'formatter': 'djangolog',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'log_file'],
            'propagate': True,
            'level': LOG_LEVEL,
        },
    }
}
