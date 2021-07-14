from django.urls import path
from . import views

urlpatterns = [
    # we need to use as_view for class based view
    path('', views.HomePageView.as_view(), name='home'),
]
