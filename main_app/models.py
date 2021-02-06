from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
GENDER = [
    ('N','None'),
    ('M','Male'),
    ('F','Female'),
    ('O','Other'),
]
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', primary_key=True, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30 ,default='')
    dob = models.DateField()
    bio = models.TextField(max_length=255 ,default='')
    profile_pic = models.CharField(max_length=255 ,default='')
    background_pic = models.CharField(max_length=255, default='')
    storage_name = models.CharField(max_length=30 ,default='')
    dark_theme = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=1,
        choices=GENDER,
        default=GENDER[0][0]
    )
    def __str__(self):
        return super().__str__(self)

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30 ,default='')
    image = models.CharField(max_length=255, default='')
    body = models.CharField(max_length=255, default='', blank=False)
    date = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)
    
    def __str__(self):
        return super().__str__(self)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    body = models.CharField(max_length=255, default='', blank=False)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return super().__str__(self)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return super().__str__(self)