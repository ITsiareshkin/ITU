from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    login = models.CharField(max_length=15)
    pwd = models.CharField(max_length=15)
    verified = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="user_photo/")
