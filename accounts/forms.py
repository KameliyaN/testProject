from django import forms
from django.contrib.auth.models import User

from accounts.models import Profile


class UserForm(forms.ModelForm):
    model = User
    fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = Profile

        exclude = ('user',)
