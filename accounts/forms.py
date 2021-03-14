from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import CustomUser


class UserRegisterForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['email','name', 'city', 'password1', 'password2']


class UserRegsterChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'city']