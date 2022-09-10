"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from epz1 import views as epz_views
from django.conf.urls import handler404, handler500
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from .views import StaticViewSitemap



sitemaps = {

    'static': StaticViewSitemap,
}


urlpatterns = [
    path('', include('epz1.urls')),
    path('about-', include('epz2.urls')),
    path('contact-', include('epz3.urls')),
    path('terms-', include('epz4.urls')),
    path('faqs/', include('epz5.urls')),
    path('cookie-', include('epz6.urls')),
    path('subscription-', include('epz7.urls')),
    path('robots.txt/', include('robots.urls')),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='cached-sitemap'),
    path('admin-MrRobot/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, serve, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, serve, document_root=settings.MEDIA_ROOT)


handler404 = epz_views.handler404
handler500 = epz_views.handler500
