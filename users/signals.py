
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
from .models import Profile

def CreateProfile(sender,instance,created,**kwargs) :
    if created:
        user=instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,

        )
def updateUser(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user

    if created==False:
        user.first_name=profile.name
        user.username=profile.username
        user.email=profile.email
        user.save()

def deleteUser(sender,instance,**kwargs):
    user=instance.user
    user.delete()

post_save.connect(updateUser,sender=Profile)
post_save.connect(CreateProfile,sender=User)
