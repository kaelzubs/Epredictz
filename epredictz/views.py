from django.urls import reverse
from epz1.models import Home_Page
from django.contrib.sitemaps import Sitemap
from django.http import HttpResponse
from django.views.decorators.http import require_GET


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: ",
        "Sitemap: http://www.epredictz.com/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")



class StaticViewSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Home_Page.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.match_dat