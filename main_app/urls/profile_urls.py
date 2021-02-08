from django.urls import path 
from ..views import profile_views

urlpatterns = [
    path("", profile_views.profile, name="profile"),
    path("profile_edit/", profile_views.profile_edit, name="profile_edit"),
    path("<int:user_id>/profile_delete/", profile_views.profile_delete, name="profile_delete")
]