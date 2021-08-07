"""
That's also works......................! 
Just run on your terminal,

$ python 'Django - Hello.py' runserver # 'Django - Hello.py' is the filename
"""

# settings.py
from django.conf.urls import url
from django.http import HttpResponse
import sys
from django.conf import settings

settings.configure(
    # DEBUG=True,
    ALLOWED_HOSTS = ['*'],
    # SECRATE_KEY='thisisasecretkey',
    ROOT_URLCONF=__name__,
    # MIDDLEWARE_CLASSES=(
        # 'django.middleware.common.CommonMiddleware',
        # 'django.middleware.csrf.CsrfViewMiddleware',
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # ),
)

# views.py
def index(request):
    print(request)
    print(dir(request))
    
    return HttpResponse("<h1>Hello Django.</h1>")


# urls.py
urlpatterns = [
    url(r'^$', index),
]

# manage.py
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)  # python
