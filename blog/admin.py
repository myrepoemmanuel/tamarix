from django.contrib import admin

from .models import ClientDetails, PersonalProfile

# Register your models here.

admin.site.register(ClientDetails)
admin.site.register(PersonalProfile)