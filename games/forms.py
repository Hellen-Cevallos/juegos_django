from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegiserForm(UserCreationForm):
    username =forms.CharField(label=contrasena)
    password1: forms.IntegerField(lab)