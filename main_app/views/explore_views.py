from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.conf import settings
from ..models import Collection
from ..forms import CollectionForm

def explore(request):
    collections = Collection.objects.filter(public = True)
    context = {
        'collections': collections,
    }
    return render(request,'public_collection/explore.html', context)