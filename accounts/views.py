from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic

from accounts.forms import SignUpForm
from accounts.models import Profile


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.picture = form.cleaned_data.get('picture')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


class UserDetails(generic.DetailView):
    model = Profile
    template_name = 'accounts/user_profile.html'
    context_object_name = 'user'
