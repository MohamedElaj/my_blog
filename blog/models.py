from django.db import models
from datetime import date

# Create your models here.


class Article(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    body = models.TextField()
    release_date = models.DateField(default=date.today)
