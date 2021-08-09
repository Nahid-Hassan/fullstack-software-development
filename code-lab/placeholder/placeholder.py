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

from io import BytesIO
from django.http import HttpResponseBadRequest
import os
import sys
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.wsgi import get_wsgi_application
from django import forms
from PIL import Image, ImageDraw
from django.core.cache import cache

# ? os.environ.get('WANT_TO_FIND', ALT_TEXT)
# DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'q5gc3wqnj_w1-5so^3^e3w)#z!pu6l2@bm7x+su+y6=-%e%x^%')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

# configure settings
settings.configure(
    DEBUG=True,
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

class ImageForm(forms.Form):
    """Form to validate request placeholder image."""
    height = forms.IntegerField(min_value=50, max_value=2000)
    width = forms.IntegerField(min_value=50, max_value=2000)

    def generate(self, image_format='PNG'):
        """generate an image of the given type and return as row bytes."""
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        # key generate for cache
        key = "{}.{}.{}".format(width, height, image_format)
        content = cache.key(key)
        print("----"*10)
        print(content)
        print("----"*10)

        if content is None:
            image = Image.new('RGB', (width, height), 'purple')
            draw = ImageDraw.Draw(image)
            text = '{} x {}'.format(width, height)
            textwidth, textheight = draw.textsize(text)

            if textwidth < width and textheight < height:
                texttop = (height - textheight) // 2
                textleft = (width - textwidth) // 2
                draw.text((textleft, texttop), text, fill=(255, 255, 255))
            content = BytesIO()
            print("+---+"*10)
            print(content)
            print("+---+"*10)
            image.save(content, image_format)
            content.seek(0)
            cache.set(key, content, 60*60)
        return content


def placeholder(request, width, height):
    form = ImageForm({'height': height, 'width': width})

    if form.is_valid():
        # height = form.cleaned_data['height']
        # width = form.cleaned_data['width']

        # print('-'*50)
        # print(height, width)
        # print('-'*50)
        # ? TODO: Generate image of requested size.
        image = form.generate()
        image.seek(0)
        # print(image)
        return HttpResponse(image, content_type='image/png')
    else:
        return HttpResponseBadRequest("Ok. But you must provide value in range(50-2000)")


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
    path('image/<int:width>/<int:height>/', placeholder),
    # path('image/<int:width>x<int:height>/', placeholder),
]

# wsgi server
application = get_wsgi_application()

# manage.py
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
