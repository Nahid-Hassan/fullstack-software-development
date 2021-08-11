import sys  # for argv
import os  # for urandom and get environment variable value

from django.http import HttpResponse  # for view
from django.urls import path  # for url route
from django.conf import settings  # for settings configuration
from django.core.management import execute_from_command_line  # for run command
from django.core.wsgi import get_wsgi_application  # for remote server

# Step - 1 Create a (view)


def index(request):
    """
        The Django function based view take a HttpRequest and Return a HttpResponse

        * Import HttpRespose from django.http import HttpRespose
    """
    return HttpResponse("<h1>Simple Django single file approach hello world project.<h1>")


# Step - 2 urlpatterns = []
urlpatterns = [
    path('', index, name='index'),
]

# Step - 3 (Settings)
DEBUG = os.environ.get("DEBUG", "on") == "on"
SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(32))
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    # DEBUG = True,
    DEBUG=DEBUG,
    # SECRET_KEY = 'as9a3*^*qxl^%$^*l',
    SECRET_KEY=SECRET_KEY,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS = ALLOWED_HOSTS,
)

# Step - 4 Run the Server in local
application = get_wsgi_application()
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
