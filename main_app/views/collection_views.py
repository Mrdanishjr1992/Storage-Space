from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.conf import settings
from ..models import Collection
from ..forms import CollectionForm

@login_required
def collection(request):
    collections = Collection.objects.filter(user = request.user)
    form = CollectionForm()
    context = {
        'collections': collections,
        'form': form
    }
    return render(request,'collection/collection_index.html', context)


@login_required
def collection_create(request):

    if request.method == 'POST':
        form = CollectionForm(request.POST)
        new_coll = form.save(commit=False)
        new_coll.user = request.user
        if form.is_valid():
            form.save()
    return redirect('collection')

@login_required
def collection_detail(request, collection_id):
    instance = Collection.objects.get(id=collection_id)
    form = CollectionForm(instance=instance)
    if request.method == 'POST':
        form = CollectionForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
    context = {
        'collection' : instance,
        'form' : form
    }
    return render(request, 'collection/collection_detail.html', context)

def collection_delete(request, collection_id):
    instance = Collection.objects.get(id=collection_id)
    if request.method == 'POST':
        instance.delete()
    return redirect('collection')
