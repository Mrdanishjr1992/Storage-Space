from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.conf import settings
from ..models import UserInfo, User
from ..forms import UserInfoForm, RegistrationForm

@login_required
def profile(request):
    user = User.objects.get(username=request.user)
    form = RegistrationForm(request.POST, user)
    info_form = UserInfoForm()
    context = {
        'user' : user,
        'form' : form,
        'info_form':info_form
    }
    return render(request, 'registration/profile.html', context)

@login_required
def profile_edit(request):
    if request.method == 'POST':
        user = RegistrationForm(request.POST)
        user_info = UserInfoForm(request.POST)
        if user.is_valid() or user_info.is_valid():
            user.save()
            user_info.save()
    
    return redirect('profile')

@login_required
def profile_delete(request):
    user = User.objects.get(username=request.user)
    user.delete()
    
    return redirect('register')
