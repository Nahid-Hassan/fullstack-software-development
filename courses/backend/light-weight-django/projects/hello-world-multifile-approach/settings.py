import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


ROOT_URLCONF = 'urls'  # indicate urls.py
# DEBUG = True
# SECRET_KEY = '98234jlds^I*'

# Little Improvement
ROOT_URLCONF = 'urls'  # indicate urls.py
DEBUG = os.environ.get("DEBUG", "on") == "on"
SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(32))

INSTALLED_APPS = [
    'django.contrib.staticfiles',
]


MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
