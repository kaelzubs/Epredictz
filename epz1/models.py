from django.db import models
from django.utils.timezone import now

# Create your models here.


class Home_Page(models.Model):
    date_time = models.DateTimeField(default=now)
    league = models.CharField(max_length=100)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    tip = models.CharField(max_length=100)
    tip_odd = models.DecimalField(max_digits=20, decimal_places=10)
    result = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        ordering = ('league',)

    def __str__(self):
        return self.league

    def get_absolute_url(self):
        return f"/{self.slug}/"
