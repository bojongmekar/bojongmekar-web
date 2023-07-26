from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    photo_link = models.URLField(max_length=200, default='')
    seller = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    description = models.TextField()