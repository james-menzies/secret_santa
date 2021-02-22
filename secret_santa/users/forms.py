from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from users.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'profile_picture']

