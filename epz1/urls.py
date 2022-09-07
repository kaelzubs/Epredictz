from django.urls import path
from .views import list_home, StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.syndication.views import Feed


sitemaps = {

    'static': StaticViewSitemap,
}


urlpatterns = [

    path('', list_home, name='list_home'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
]