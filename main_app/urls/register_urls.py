from django.urls import path 
from . import register_views

urlpatterns = [
    # HOME-PAGE
    path("/", register_views.home, name="home"),
    
    # ABOUT-PAGE
    path("about/", register_views.about, name="about"),
]
