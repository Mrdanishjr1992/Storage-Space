from django.contrib import admin
from .models import Collection, Comment, Like, UserInfo

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Collection)
admin.site.register(Comment)
admin.site.register(Like)

