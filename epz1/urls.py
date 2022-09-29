from django.urls import path
from .views import list_home
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [

    path('', list_home, name='list_home'),
    path("ads.txt", RedirectView.as_view(url=staticfiles_storage.url("ads.txt"))),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)