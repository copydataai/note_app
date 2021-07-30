"""Development settings."""

from .base import *
from .base import env

# Base
DEBUG = True

# Security
SECRET_KEY = env('DJANGO_SECRET_KEY', default='95f3114c7a2815bc88585b1f99f3d70688f98dd293ff28ed80cae7e4672d42c6574923414bee83f5b94edf18774fc88d0499c697a7f030accc825ba2166cd657')
ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
]

# Django-extensions
INSTALLED_APPS += ['django_extensions']

# Templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
