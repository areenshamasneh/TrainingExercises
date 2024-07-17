from django.db import models
from django.utils import timezone
import datetime


class Article(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    slug = models.SlugField()
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
