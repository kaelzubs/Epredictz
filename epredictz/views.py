from django.contrib.sitemaps import Sitemap
from epz1.models import Home_Page
from django.http import HttpResponse
from django.views import View



class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Home_Page.objects.all()


class AdsView(View):
    """Replace pub-0000000000000000 with your own publisher ID"""
    line  =  "google.com, pub-6411693288489882, DIRECT, f08c47fec0942fa0"

    def get(self, request, *args, **kwargs):
        return HttpResponse(self.line)
