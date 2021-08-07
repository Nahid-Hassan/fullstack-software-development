"""
README.md

# To make this script as reusable template. You need to do the following things

nahid@infogarden:~/Desktop$ tree project_name/
project_name/
└── hello.py

nahid@infogarden:~/Desktop$ django-admin.py startproject foo --template=project_name
nahid@infogarden:~/Desktop$ tree foo/
foo/
└── hello.py

nahid@infogarden:~/Desktop$ python foo/hello.py runserver 
"""

import os
import sys
from django.conf import settings
from django.http import HttpResponse
from django.conf.urls import url
from django.urls import path
from django.core.wsgi import get_wsgi_application

# ? os.environ.get('WANT_TO_FIND', ALT_TEXT)
DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key }}')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# configure settings
settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,  # __main__
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


# views.py
def index(request):
    return HttpResponse("""
        <div style="padding: 10px; margin: 10px 150px; font-align:center;">
            <h1>Django - Reusable Template Creation Project</h1>
            <hr>
            <p>You are welcome!</p>
        </div>
    """)


# urls.py
urlpatterns = [
    path('', index, name='index'),
]

# wsgi server
application = get_wsgi_application()

# manage.py
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
