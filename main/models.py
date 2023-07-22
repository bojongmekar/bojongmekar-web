from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)