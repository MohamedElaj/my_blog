from django.db import models
from datetime import date
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class Article(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    body = CKEditor5Field("Text", config_name="extends")
    release_date = models.DateField(default=date.today)

    def __str__(self):
        return self.title
