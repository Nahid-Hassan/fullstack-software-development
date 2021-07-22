# News Paper Projects and Custom User Model

## Table of Contents

- [News Paper Projects and Custom User Model](#news-paper-projects-and-custom-user-model)
  - [Table of Contents](#table-of-contents)
    - [Setup](#setup)
    - [Custom User Model](#custom-user-model)

### Setup

The first step is to create a new Django project from the command line. We need to
do several things:
- Create and navigate into a new directory for our code
- Create a new virtual environment `news`
- Install Django
- Make a new Django **project** `newspaper_project`
- Make a new **app** `users`

We’re calling our app for managing users `users` here but you’ll also see it frequently
called `accounts` in open source code. The actual name doesn’t matter as long as you
are consistent when referring to it throughout the project.

```bash
$ cd projects
$ mkdir news
$ cd news
$ pipenv install django
$ pipenv shell
$ django-admin startproject newspaper_project .
$ python manage.py startapp users
$ python manage.py runserver
```

Note that we `did not run migrate to configure our database`. It’s important to wait until
after we’ve created our new custom user model before doing so given how 
`tightly connected the user model is to the rest of Django`.

### Custom User Model

Creating our custom user model requires four steps:

- Update `settings.py`
- Create a new `CustomUser model`
- Create new forms for `UserCreation` and `UserChangeForm`
- Update the `admin`

In settings.py we’ll add the users app to our `INSTALLED_APPS` . Then at the bottom
of the file use the `AUTH_USER_MODEL` config to tell Django to use our new custom user
model in place of the `built-in User model`. We’ll call our custom user model `CustomUser`
so, since it exists within our users app we refer to it as `users.CustomUser`.

```py
# newspaper_project/settings.py
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'users', # new
]

# ...
AUTH_USER_MODEL = 'users.CustomUser'
```

Now update `users/models.py` with a new User model which we’ll call `CustomUser` .
We’ll also add our first extra field for the `“age”` of our users. We can use Django’s
`PositiveIntegerField` which means the integer must be either positive or zero.

```py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0)
```

That’s really all the code we need! Since we’re extending `AbstractUser` our `CustomUser`
is basically `a copy of the default User model`. The only `update` is our new `age field`.

