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

If you look within our **directory** there are now `two` new files: `Pipfile` and `Pip-
file.lock` . We have the information we need for a new virtual environment but we
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