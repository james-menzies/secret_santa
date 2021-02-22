from django import forms
from django.forms import ModelForm

from users.models import CustomUser


class UserRegistrationForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'confirm_password', 'profile_picture']

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
