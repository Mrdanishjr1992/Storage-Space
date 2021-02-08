from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.conf import settings
from ..models import Collection, Comment
from ..forms import CollectionForm

def explore(request):
    collections = Collection.objects.filter(public = True)
    context = {
        'collections': collections,
    }
    return render(request,'public_collection/explore.html', context)

def explore_comment(request, collection_id):
    collections = Collection.objects.filter(public = True)
    comments = Comment.objects.filter(collection_id=collection_id)
    context = {
        'collections': collections,
        'comments': comments
    }
    return render(request,'public_collection/explore.html', context)