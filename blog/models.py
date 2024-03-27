from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.

class ClientDetails(models.Model):
    user = models.CharField(max_length=200, null=True, blank=True)
    client_code = models.CharField(max_length=200, blank=True, null=True)
    date_from = models.CharField(max_length=200, null=True, blank=True)
    date_to = models.CharField(max_length=200, null=True, blank=True)
    number_of_hours = models.CharField(max_length=200, null=True, blank=True)
    number_of_session = models.CharField(max_length=200, null=True, blank=True)
    counselor_name = models.CharField(max_length=200, null=True, blank=True)
    counselor_Association = models.CharField(max_length=200, null=True, blank=True)
    counselor_Association_body = models.CharField(max_length=200, unique=True, null=True, blank=True)
    supervisor_name = models.CharField(max_length=200, null=True, blank=True)
    supervisor_Association = models.CharField(max_length=200, null=True, blank=True)
    supervisor_Association_body = models.CharField(max_length=200, unique=True, null=True, blank=True)
    presenting_problem = models.TextField(max_length=100000, null=True, blank=True)
    
    def __str__(self):
        return self.counselor_name

    class Meta:
        verbose_name_plural = 'Client Details'


class PersonalProfile(models.Model):
    name_of_Counselor = models.CharField(max_length=200, null=True, blank=True)
    KCPA_no_Counselor = models.CharField(max_length=200, blank=True, null=True)
    name_of_Supervisor = models.CharField(max_length=200, null=True, blank=True)
    KCPA_no_Supervisor = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name_of_Counselor

    class Meta:
        verbose_name_plural = 'Personal Profile'