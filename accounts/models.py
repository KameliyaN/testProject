from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200,blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True,default="/user_profile.png")

    def __str__(self):
        return f'{self.user.username}'
