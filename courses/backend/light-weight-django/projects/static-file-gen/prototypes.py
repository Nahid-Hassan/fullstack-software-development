from posixpath import join
from django.conf import settings
from pathlib import Path
import os
import sys

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
print('----==='*30)

settings.configure(
    DEBUG=True,
    SECRET_KEY='b0mqvak1p2sqm6p#+8o8fyxf+ox(le)8&jh_5^sxa!=7!+wxj0',
    ROOT_URLCONF='sitebuilder.urls',
    ALLOWED_HOST=['*'],
    MIDDLEWARE=(
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ),

    INSTALL_APPS=(
        'django.contrib.staticfiles',

        # local
        'sitebuilder',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'sitebuilder/templates')],
            'APP_DIRS': True,
        },
    ),

    STATIC_URL='/static/',
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
    STATICFILES_DIRS=[(os.path.join(BASE_DIR,'sitebuilder/static'))]
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
