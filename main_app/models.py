from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class UserInfo(models.Model):
    GENDER = [
        ('N','None'),
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ]
    nickname = models.CharField(max_length=30)
    bio = models.TextField(max_length=255)
    profile_pic = models.CharField(max_length=255)
    background_pic = models.CharField(max_length=255)
    storage_name = models.CharField(max_length=30)
    dark_theme = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=1,
        choices=GENDER,
        default=GENDER[0][0]
    )
    user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)


class Collection(models.Model):
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    


class Comment(models.Model):
    body = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    collection_id = models.ForeignKey(Collection, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    


class Like(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    collection_id = models.ForeignKey(Collection, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
