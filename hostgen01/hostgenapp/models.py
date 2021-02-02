from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class hosts(models.Model):
   h_host = models.CharField(max_length=15)
   h_ip = models.CharField(max_length=15)

class networks(models.Model):
    net_name = models.CharField(max_length=15)
    net_ip = models.CharField(max_length=15)

class MyUserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    dep_name = models.CharField(max_length=15,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.user.username
