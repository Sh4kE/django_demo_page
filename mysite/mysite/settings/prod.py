from __future__ import absolute_import
from .common import *


DEBUG = False

ALLOWED_HOSTS = [ 'django.sh4ke.acrux.uberspace.de' ]

CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS

USE_X_FORWARDED_HOST = True
