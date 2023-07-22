from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=50)
    photo_link = models.URLField(max_length=200, default='')
    content = models.TextField()
    date = models.DateField(auto_now_add=True)