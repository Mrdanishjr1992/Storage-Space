from django.urls import path 
from ..views import explore_views, comment_views, like_views
from django.urls import reverse

urlpatterns = [
    # HOME-PAGE
    path("", explore_views.explore, name="explore")
]