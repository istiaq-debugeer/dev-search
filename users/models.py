from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=50)
    username=models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro=models.CharField(max_length=200,blank=True)
    bio=models.TextField(blank=True,null=True)
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    social_github=models.CharField(max_length=200,blank=True,null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkdein = models.CharField(max_length=200, blank=True, null=True)
    social_website =   models.CharField(max_length=200, blank=True, null=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Skill(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


