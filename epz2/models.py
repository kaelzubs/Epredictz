from operator import mod
from django.db import models

# Create your models here.

class About_Page(models.Model):
    title = models.CharField(max_length=60)
    bodytext = models.TextField()
    created = models.DateTimeField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
