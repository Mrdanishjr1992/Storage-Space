from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.conf import settings
from ..models import UserInfo
from ..forms import RegistrationForm, UserInfoForm


# Create your views here.
def register(request):
    error_message = ''
    # session_key = request.session._get_session_key()

    # if session_key:
    #     return redirect('profile')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_info = UserInfo(user_id= user)
            user_info.save()
            login(request, user)
            return redirect('profile', user_id= user.id)
        else:  
            error_message = 'Invalid signup credintials, Try agin.'
            
    form = RegistrationForm()
    context = {
        'form' : form,
        'error_message': error_message
    }
    return render(request, 'registration/register.html', context)


def about(request):
    return render(request, 'about.html')