from os import getenv,path

from dotenv import load_dotenv

from .base import * # noqa

from .base import BASE_DIR

local_env_file = path.join(BASE_DIR, '.envs', 'env.local')

if path.isfile(local_env_file):
    load_dotenv(local_env_file)
    
DEBUG = True   
SITE_NAME= getenv('SITE_NAME')
SECRET_KEY = getenv("DJANGO_SECRET_KEY", "2FqhCBRPtSQzslgwXE5QG_Opl-tNooV8DiiJFbUzO24oLo9-rhI") 



ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]
ADMIN_URL = getenv("DJANGO_ADMIN_URL")
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = getenv("EMAIL_HOST")
EMAIL_PORT = getenv("EMAIL_PORT")
DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL")
DOMAIN = getenv("DOMAIN")

LOGGING = {'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] %(name) -12s %(module)s %(thread)d '
                       'path:%(pathname)s lineno:%(lineno)s '
                       'func:%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    "root" : {"level" : "INFO", "handlers" : ["console"]},
    }