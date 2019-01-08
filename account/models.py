from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    target = models.CharField(max_length=1000)
    photoDescription = models.CharField(max_length=1000,default=None)
    followPerDay = models.IntegerField(default=None)
    postsPerDay = models.IntegerField(default=3)
    timer = models.IntegerField(default=0)
    followers = models.IntegerField()
    followings = models.IntegerField()
