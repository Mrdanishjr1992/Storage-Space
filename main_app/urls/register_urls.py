from django.urls import path 
from ..views import register_views

urlpatterns = [
    # HOME-PAGE
    path("", register_views.register, name="register"),
    
    # ABOUT-PAGE
    path("about/", register_views.about, name="about"),
]
