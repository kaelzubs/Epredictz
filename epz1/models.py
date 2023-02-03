from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Home_Page(models.Model):
    slug = AutoSlugField(populate_from='league')
    match_date_time = models.DateTimeField(auto_now_add=True, null=True)
    league = models.CharField(max_length=100)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    tip = models.CharField(max_length=100)
    tip_odd = models.DecimalField(max_digits=20, decimal_places=10)
    result = models.CharField(max_length=100)

    class Meta:
        ordering = ('league',)

    def __str__(self):
        return self.league

    def get_absolute_url(self):
        return f"/{self.slug}/"
