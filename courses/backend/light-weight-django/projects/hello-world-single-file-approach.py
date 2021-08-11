import sys # for argv

from django.http import HttpResponse # for view
from django.urls import path # for url route
from django.conf import settings # for settings configuration
from django.core.management import execute_from_command_line # for run command


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
settings.configure(
    DEBUG = True, 
    SECRET_KEY = 'as9a3*^*qxl^%$^*l',
    ROOT_URLCONF = __name__,
)

# Step - 4 Run the Server in local
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)