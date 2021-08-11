import os

ROOT_URLCONF = 'urls' # indicate urls.py
# DEBUG = True
# SECRET_KEY = '98234jlds^I*'

# Little Improvement
ROOT_URLCONF = 'urls' # indicate urls.py
DEBUG = os.environ.get("DEBUG", "on") == "on"
SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(32))
