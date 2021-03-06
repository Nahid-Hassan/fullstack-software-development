import os
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template, context
from django.utils._os import safe_join


def get_page_or_404(name):
    """Return page content as django template or raise 404 error."""
    # print(safe_join(settings.SITE_PAGES_DIRECTORY, name))
    # print('-'*30)
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
    except ValueError:
        raise Http404("file path is not found Page not found.")
    else:
        if not os.path.exists(file_path):
            raise Http404("Page path not exists not found.")

    with open(file_path, 'r') as f:
        page = Template(f.read())

    return page


def page(request, slug='index'):
    """Render the requested page if found."""
    file_name = '{}.html'.format(slug)
    page = get_page_or_404(file_name)
    context = {
        'slug': slug,
        'page': page
    }

    print(context)
    print('8'*40)

    return render(request, 'index.html', context)
