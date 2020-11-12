from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic

from accounts.forms import SignUpForm, ProfileForm, UserForm
from accounts.models import Profile


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

    return render(request, 'accounts/signup.html', {'form': form})


def profile(request):
    profile = request.user.profile

    context = {'profile': profile}

    return render(request, 'accounts/user_profile.html', context)


@login_required(login_url="home")
def profile_edit(request):
    user = request.user
    profile = user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()

        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user-profile')

    context = {'form': form,
               }
    return render(request, 'accounts/edit_profile.html', context)
