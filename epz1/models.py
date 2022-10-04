from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Home_Page(models.Model):
    slug = models.SlugField(default='', editable=False, max_length=200, null = False)
    match_dat = models.CharField(max_length=100)
    match_time = models.CharField(max_length=100)
    league = models.CharField(max_length=100)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    tip = models.CharField(max_length=100)
    tip_odd = models.CharField(max_length=100)
    result = models.CharField(max_length=100)

    def __str__(self):
        return self.match_dat
    
    def get_absolute_url(self):
        kwargs = {
        'pk': self.id,
            'slug': self.slug
        }
        return reverse('list_home', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.league
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-id']

