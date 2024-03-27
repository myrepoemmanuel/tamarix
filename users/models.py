from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    address_one = models.CharField(max_length=200, null=True, blank=True)
    address_two = models.CharField(max_length=200, null=True, blank=True)
    postcode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=200, null=True, blank=True)
    
    
    
    def __str__(self):
        return f'{self.user.username} Profile'
#    
# #    
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, *args, **kwargs):
#    if created:
#        Profile.objects.create(user=instance, first_name=str(instance.full_name).split(" ")[0], last_name=str(instance.full_name).split(" ")[1])
#        print(instance.user_name, 'Profile created')


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, *args, **kwargs):
#     instance.profile.save()

