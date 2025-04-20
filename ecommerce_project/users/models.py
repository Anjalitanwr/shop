from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import *
  

class UserProfile(AbstractUser):
        fname=models.CharField(max_length=100,null=True)
        lname=models.CharField(max_length=100,null=True)
        address = models.TextField()
        image = models.ImageField(upload_to='profile_img/',null=True, blank=True)
        phone = models.CharField(max_length=15, blank=True)
        address = models.TextField(blank=True)


        def __str__(self):
            return self.username
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()  
