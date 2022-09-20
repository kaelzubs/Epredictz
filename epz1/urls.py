from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from .views import list_home




urlpatterns = [

    path('', list_home, name='list_home'),
    path('ads.txt', RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),),

]