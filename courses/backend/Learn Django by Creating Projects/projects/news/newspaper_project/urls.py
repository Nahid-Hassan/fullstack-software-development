from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('pages.urls')),
    path('users/',include('users.urls')),
    path('users/',include('django.contrib.auth.urls')),
]
