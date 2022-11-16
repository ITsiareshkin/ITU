from django.db import models

# Create your models here.
class user(models.Model):
    title = models.CharField(max_length=255)