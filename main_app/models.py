from django.db import models
from django import forms
from django.urls import reverse
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nickname


class Collection(models.Model):
    PUBLIC = [
        ('True','True'),
        ('False','False')
    ]
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    public = models.CharField(
        max_length=5,
        choices=PUBLIC,
        default=PUBLIC[1][0]
    )
    user = models.ForeignKey(User,  on_delete = models.CASCADE)
    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.CharField(max_length=255)
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.body


class Like(models.Model):
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

