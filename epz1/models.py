from django.db import models
# Create your models here.

class Home_Page(models.Model):
    match_dat = models.CharField(max_length=100)
    match_time = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    tip = models.CharField(max_length=100)
    tip_odd = models.CharField(max_length=100)
    result = models.CharField(max_length=100)

    def __str__(self):
        return self.match_dat

    def get_absolute_url(self):
        return "/?page=%i" % self.id

