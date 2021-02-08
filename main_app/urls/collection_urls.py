from django.urls import path 
from ..views import collection_views
from django.urls import reverse

urlpatterns = [
    # HOME-PAGE
    path("", collection_views.collection, name="collection"),
    path("collection_create/", collection_views.collection_create, name="collection_create"),
    path("<int:collection_id>/detail", collection_views.collection_detail, name="collection_detail"),
    path("<int:collection_id>/delete", collection_views.collection_delete, name="collection_delete")
]