from django.urls import path 
from ..views import profile_views

urlpatterns = [
    path("", profile_views.profile, name="profile"),
    path("profile/edit", profile_views.profile_edit, name="profile_edit"),
]