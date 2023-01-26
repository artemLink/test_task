from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Пошта ")
    password1 = forms.CharField(label="Пароль ")
    password2 = forms.CharField(label="Підтвердження паролю ")

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


