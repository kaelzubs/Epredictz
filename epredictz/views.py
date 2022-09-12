from django.contrib.sitemaps import Sitemap
from epz1.models import Home_Page


class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Home_Page.objects.all()
