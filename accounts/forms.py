from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2','picture')

