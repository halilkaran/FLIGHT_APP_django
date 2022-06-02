from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
THIRD_PARTY_APPS = [
    "debug_toolbar",
]

INSTALLED_APPS += THIRD_PARTY_APPS

THIRD_PARTY_MIDDLEWARE = [
    #for debug toolbar
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

INTERNAL_IPS = [
    "127.0.0.1",
]