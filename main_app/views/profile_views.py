from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.conf import settings
from ..models import UserInfo, User
from ..forms import UserInfoForm, RegistrationForm

def profile(request):
    user = User.objects.get(id=request.user.id)
    form = RegistrationForm(instance = user)
    info_form = UserInfoForm(instance = user)
    context = {
        'user' : user,
        'form' : form,
        'info_form' : info_form
    }
    return render(request, 'registration/profile.html', context)

def profile_edit(request):
    if request.method == 'POST':
        user = RegistrationForm(request.POST)
        user_info = UserInfoForm(request.POST)
        if user.is_valid() and user_info.is_valid():
            user.save()
            user_info.save()
    
    return redirect('profile')
