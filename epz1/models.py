from django.db import models
from datetime import datetime

# Create your models here.

class IpModel(models.Model):
    ip = models.CharField(max_length=100)
    def __str__(self):
        return self.ip


class Home_Page(models.Model):
    date_time = models.DateTimeField(default=datetime.now)
    league = models.CharField(max_length=100)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    tip = models.CharField(max_length=100)
    tip_odd = models.FloatField(default=None)
    result = models.CharField(max_length=100)
    slug = models.SlugField()
    pub_date = models.DateField()
    vote = models.ManyToManyField(IpModel, related_name="vote_likes", blank=True)

    class Meta:
        ordering = ('-date_time',)

    def __str__(self):
        return self.league

    def get_absolute_url(self):
        return f"/{self.slug}/"

    def total_vote(self):
        return self.vote.count()
