# Light Weight Django

## Table of Contents

- [Light Weight Django](#light-weight-django)
  - [Table of Contents](#table-of-contents)
  - [Chapter 1: The World Smallest Django Project](#chapter-1-the-world-smallest-django-project)
    - [The World Smallest Django Project](#the-world-smallest-django-project)
      - [Hello World (Single file approach)](#hello-world-single-file-approach)
      - [Hello World (Mutlifile Approach)](#hello-world-mutlifile-approach)
      - [Improvement(Local Server to Remote Server)](#improvementlocal-server-to-remote-server)
      - [Additional Configuartion](#additional-configuartion)
      - [Other important information](#other-important-information)

---
Chapter 1: The World Smallest Django Project
---

### The World Smallest Django Project

#### Hello World (Single file approach)

To create a simple `Hello World` project we need to create a **view** to serve the **root URL** and necessary **settings** to **configure** the Django **environment**.

1. **Step - 1(Create View)**:

The Django function based view take a **HttpRequest** and Return a **HttpResponse**

```py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Simple Django single file approach hello world project.")
```

2. **Step - 2(Associate view with Root URL)**:

In order to tie our view into the site’s structure, we’ll need to associate it with a **URL pattern**.

```py
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
```

3. **Step - 3 (Django Settings)**:

Contains some simple lines we’ll need to make our project **runnable**.

- Minimum settings requirement
  - `DEBUG`=True / ALLOWED_HOSTS=`['localhost', '*', 'example.com']`
  - `ROOT_URLCONF` = `__name__`
  - `SECRET_KEY` = `RandomKey`

**Note**: A secret key must be generated for the `default session` and cross-site request forgery (**CSRF**) protection.

```py
from django.conf import settings

settings.configure(
    DEBUG = True, 
    SECRET_KEY = 'as9a3*^*qxl^%$^*l'
    ROOT_URLCONF = __name__,
)
```

4. **Running the Example**:

A typical Django project contains a `manage.py` file, which is used to `run various commands` such as creating 
**database tables** and running the **development server**.

```py
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
```

Finally run the project

```bash
$ python hello-world-single-file-approach.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 11, 2021 - 12:12:55
Django version 3.1.4, using settings None
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

#### Hello World (Mutlifile Approach)

1. `views.py`

```py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Mutlifile Project")
```

2. `urls.py`

```py
from django.urls import path
from views import index

urlpatterns = [
    path('', index, name='index'),
]
```

3. `settings.py`

```py
ROOT_URLCONF = 'urls' # indicate urls.py
DEBUG = True
SECRET_KEY = '98234jlds^I*'
```

4. `manage.py`

```py
import os, sys
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    # set environment varialbe
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')  # new
    execute_from_command_line(sys.argv)
```

#### Improvement(Local Server to Remote Server)

```bash
nahid@cse ~$ pip install gunicorn
```

Add this two lines of code in your `manage.py` file or above the `manage.py portion`

```py
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

def __name__ == '__main__':
    # ... 
```

```bash
nahid@cse ~$ gunicorn hello-world-single-file-approach --log-file=-

[2021-08-11 13:03:26 +0600] [119309] [INFO] Starting gunicorn 20.1.0
[2021-08-11 13:03:26 +0600] [119309] [INFO] Listening at: http://127.0.0.1:8000 (119309)
[2021-08-11 13:03:26 +0600] [119309] [INFO] Using worker: sync
[2021-08-11 13:03:26 +0600] [119326] [INFO] Booting worker with pid: 119326
```

#### Additional Configuartion

While **Gunicorn** is a `production-ready web server`, the application itself is not yet pro‐
duction ready, as **DEBUG** should never be enabled in production. As previously noted,
the `SECRET_KEY` is also nonrandom and should be made random for additional security.

```py
import os

# dictionary method
DEBUG = os.environ.get("DEBUG", "on") == "on"
SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(32))

settings.configure(
    DEBUG = DEBUG,
    SECRET_KEY = SECRET_KEY,
    # ........
)
```

If **DEBUG** is false then we must sepcify the **ALLOWED_HOSTS=[]**. To doing this,

```py
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    # ........
    ALLOWED_HOSTS = ALLOWED_HOSTS,
    # ........
)
```

#### Other important information

Export environment variable in your system.

```bash
# exporting
> export DEBUT=on
> export SECRET_KEY = 'some secret key'

# unset
> unset DEBUG
```