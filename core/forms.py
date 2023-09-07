from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    PasswordChangeForm,
    AuthenticationForm
)

INPUT_CLASSES = """
border-b border-yellow-500 bg-gray-800 xl:w-[18rem] text-yellow-500 focus:bg-gray-800 w-[15rem] p-1
"""


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': INPUT_CLASSES
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))

class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_CLASSES
    }))