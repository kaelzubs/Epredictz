from django.db import models
from datetime import datetime

# Create your models here.


class Home_Page(models.Model):
    date_time = models.DateTimeField(default=datetime.now)
    league = models.CharField(max_length=100)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    tip = models.CharField(max_length=100)
    tip_odd = models.FloatField(default=None)
    result = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        ordering = ('-date_time',)

    def __str__(self):
        return self.league

    def get_absolute_url(self):
        return f"/{self.slug}/"
