# Learn Django Beginners to Professionals

## Table of Contents

- [Learn Django Beginners to Professionals](#learn-django-beginners-to-professionals)
  - [Table of Contents](#table-of-contents)
    - [Django for Beginners](#django-for-beginners)
      - [Why Django](#why-django)
      - [Python Hello World](#python-hello-world)
      - [Initial Setup](#initial-setup)
      - [Git and Visual Studio Code](#git-and-visual-studio-code)
      - [Hello World Application](#hello-world-application)
      - [Create an app](#create-an-app)
      - [Views and URLConfs](#views-and-urlconfs)

### Django for Beginners

Django is a free, open source web framework written in the Python programming
language and used by millions of programmers every year. Its popularity is due to its
friendliness to both beginners and advanced programmers: Django is robust enough
to be used by the largest websites in the world– `Instagram`, `Pinterest`, `Bitbucket`,
`Disqus`–but also flexible enough to be a good choice for early-stage startups and
prototyping personal projects.

#### Why Django

A web framework is a collection of modular tools that abstracts away much of the
difficulty–and repetition–inherent in web development.

Django inherited Python’s “batteries-included” approach and includes out-of-the box
support for common tasks in web development:

- User **Authentication**
- **Templates**, **Routes**, And **Views**
- **Admin** Interface
- Robust **Security**
- Support for **Multiple Database** Backends
- and much much more

#### Python Hello World

```py
# This is Python code
print("Hello, world!")
```

#### Initial Setup

**Configure** your computer to work on Django projects. We start with an overview of the **command line** and use it to install the latest versions of both `Django (2.0)` and `Python (3.6x)`. Then we discuss `virtual environments`,
`git`, and working with a `text editor`.

**Command that most frequently used**:

- `cd` (change down a directory)
- `cd ..` (change up a directory)
- `ls` (list files in your current directory)
- `pwd` (print working directory)
- `mkdir` (make directory)
- `touch` (create a new file)

**Install Python and Django**

Historically Python developers have used either virtualenv or pyenv to configure
virtual environments. But in 2017 prominent Python developer `Kenneth Reitz` released
`Pipenv` which is now the officially recommended Python packaging tool.
`Pipenv` is similar to npm and yarn from the Node ecosystem: it creates a `Pipfile`
containing software dependencies and a `Pipfile.lock` for ensuring deterministic
builds. “Determinism” means that each and every time you download the software
in a new virtual environment, you will have exactly the same configuration. Sebastian
McKenzie, the creator of Yarn which first introduced this concept to JavaScript
packaging, has a concise blog post explaining what determinism is and why it matters.
The end result is that we will create a new virtual environment with `Pipenv` for each
new Django Project.

```console
$ pip3 install pipenv
```

To see Pipenv in action, let’s create a new directory and install Django. First navigate
to the `./projects`, create a new directory `django` , and enter it with cd .

```bash
# create a directory name django and enter it with cd
$ cd projects
$ mkdir django
$ cd django

# install django
$ pipenv install django
```

If you look within our **directory** there are now `two` new files: `Pipfile` and `Pip- file.lock` . We have the information we need for a new virtual environment but we
have not activated it yet. Let’s do that with `pipenv shell` .

```bash
# activate django virtual environment
$ pipenv shell
```

Create a new Django **project** called `test_project` with the following command. **Don’t forget that period . at the end**.

```bash
$ ls
Pipfile Pipfile.lock

# Use dot for avoid create extra test_project
$ django-admin startproject test_project .
$ tree
├── manage.py
├── Pipfile
├── Pipfile.lock
└── test_project
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

Now let’s confirm everything is working by running Django’s local web server.

```bash
$ python manage.py runserver
```

If you visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) you should see the following image.

![images](images/django-default.png)

#### Git and Visual Studio Code

```bash
$ sudo apt install git # git is by default installed in linux based system

# two additional commands for newly installed git
$ git config --global user.name "Your Name"
$ git config --global user.email "yourname@email.com"
```

**Editor**:

- `Visual Studio Code` is awesome.

```bash
$ sudo snap install --classic code
```

- Experienced programmer used `vim` or `emacs`

#### Hello World Application

This is the `traditional` way to start a new programming language or `framework`. We’ll also work with `git` for the first time and deploy our code to `Github`.

- **Initial Setup**:

To start navigate to a new directory on your computer. For example, we can create a
helloworld folder on the Desktop with the following commands.
Command Line

```bash
$ cd ~/projects
$ mkdir helloworld
$ cd helloworld
```

Make sure you’re not already in an `existing virtual environment` at this point. If you see
text in parentheses () before the dollar sign $ then you are. To exit it, type exit and
hit Return . The parentheses should disappear which means that virtual environment
is no longer active.

We’ll use pipenv to `create a new virtual environment`, install `Django` and then activate
it.

```bash
# install django
$ pipenv install django
# activate environment
$ pipenv shell
# create helloworld_project
$ django-admin startproject helloworld_project .
$ tree
.
├── helloworld_project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── Pipfile
└── Pipfile.lock
```

The

- `settings.py` file controls our **project’s settings**
- `urls.py` tells Django which pages to build in response to a browser or url request,
- `wsgi.py` which stands for **web server gateway interface**, helps Django serve our eventual web pages.
- The last file `manage.py` is used to execute various Django commands such as running the local web
  server or creating a new app.

Django comes with a built-in web server for local development purposes. We can start
it with the `runserver` command.

```bash
$ ls
helloworld_project  manage.py  Pipfile  Pipfile.lock
$ python manage.py runserver
```

#### Create an app

Django uses the concept of `projects and apps` to keep code `clean and readable`. A
**single Django project contains one or more apps within it that all work together to power a web application**. This is why the command for a new Django project is
**startproject** ! For example, a real-world Django `e-commerce` site might have one app
for user `authentication`, another app for `payments`, and a third app to power item
`listing` details. Each focuses on an isolated piece of functionality.

We need to create our **first app** which we’ll call `pages` . From the command line, quit
the server with `Control+c` . Then use the startapp command.

```bash
$ python manage.py startapp pages
$ tree
pages/
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

Let’s review what each new pages app file does:

- `admin.py` is a configuration file for the built-in Django Admin app.
- `apps.py` is a configuration file for the app itself.
- `migrations/` keeps track of any changes to our `models.py` file so our database
  and `models.py stay in sync`.
- `models.py` is where we define our **database** models, which Django automatically
  translates into database tables.
- `tests.py` is for our app-specific tests.
- `views.py` is where we handle the `request/response logic` for our web app.

Even though our `new app exists within the Django project`, Django doesn’t “know”
about it until we **explicitly add** it. In your text editor open the `settings.py` file and
scroll down to **INSTALLED_APPS** where you’ll see six built-in Django apps already there.
Add our new pages app at the bottom:

```py
# helloworld_project/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages', # new
]
```

#### Views and URLConfs

In Django,

- `Views` determine what `content is displayed` on a given page while
- `URLConfs` determine `where that content is going`.

When a user **requests** a specific page, like the homepage, the **URLConf** uses a `regular expression to map that request to the appropriate view function which then returns the correct data.`

In other words, our view will output the text “Hello, World” while our url will ensure
that when the user visits the homepage they are redirected to the correct view.
Let’s start by updating the views.py file in our pages app to look as follows:

```py
# pages/views.py
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello, World!')
```

Basically we’re saying whenever the view function **homePageView** is called, return
the text `“Hello, World!”` More specifically, we’ve imported the built-in `HttpResponse method so we can return a response object to the user`. We’ve created a function called
homePageView that accepts the request object and returns a response with the string
Hello, World! .

Now we need to configure our `urls.py` Within the pages app, **create** a new `urls.py` file.

```bash
$ ls
db.sqlite3  helloworld_project	manage.py  pages  Pipfile  Pipfile.lock
$ cd pages
$ ls
admin.py  apps.py  __init__.py	migrations  models.py  tests.py  views.py
$ touch urls.py
$ ls
admin.py  apps.py  __init__.py	migrations  models.py  tests.py  views.py urls.py # new
```

Code:

```py
# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
]
```

On the top line we `import path` from Django to power our **urlpattern** and on the next
line we import our views. The period used here `from . import views` means reference
the `current directory`, which is our pages app containing both views.py and urls.py .
Our urlpattern has three parts:

```py
    path('regular expression', view, name=optional),
```

- a Python regular expression for the empty string ''
- specify the view which is called homePageView
- add an optional url name of 'home'

> In other words, if the user requests the homepage, represented by the empty string '' then use the view called homePageView .

We’re almost done. The last step is to configure our project-level `urls.py` file too.
Remember that it’s common to have multiple apps within a single Django project, so
they each need their own route.

Update the helloworld_project/urls.py file as follows:

```py
# helloworld_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
```

It’s often confusing to beginners that we don’t need to import the pages app here, yet
we refer to it in our urlpattern as pages.urls . The reason we do it this way is that that
the method `django.urls.include()` expects us to pass in a **module**, or **app**, as the `first argument`. So without using include we would need to import our pages app, but since
we do use include we don’t have to at the project level!

We have all the code we need now! To confirm everything works as expected, restart
our Django server:

```bash
$ ls 
db.sqlite3  helloworld_project	manage.py  pages  Pipfile  Pipfile.lock
$ python manage.py runserver
# ...........
Django version 3.2.3, using settings 'helloworld_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

If you visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) you should see the following image.
Starting development server at http://127.0.0.1:8000/.

![images](images/helloworld.png)