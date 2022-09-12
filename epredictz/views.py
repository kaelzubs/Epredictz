from django.urls import reverse
from epz1.models import Home_Page
from django.contrib.sitemaps import Sitemap


class StaticViewSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Home_Page.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.match_dat