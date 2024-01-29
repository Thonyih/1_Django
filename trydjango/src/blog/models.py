from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=120)
    summary = models.TextField(max_length=120)
    content = models.TextField()
