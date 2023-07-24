from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import HTML, JS, PYTHON, Comment, Assignments

INPUT_STYLES = """
rounded-md px-3 py-1
"""

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_STYLES,
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': INPUT_STYLES,
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_STYLES,
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_STYLES,
    }))     

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_STYLES,
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_STYLES,
    }))
    

class htmlForm(forms.ModelForm):
    class Meta:
        model = HTML
        fields = ('title', 'video_link', 'notes',)

class jsForm(forms.ModelForm):
    class Meta:
        model = JS
        fields = ('title', 'video_link', 'notes',)
        
class pythonForm(forms.ModelForm):
    class Meta:
        model = PYTHON
        fields = ('title', 'video_link', 'notes',)
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('username', 'body',)
        widgets = {
            "username" : forms.TextInput(attrs={
                'class': INPUT_STYLES
            }),
            "body": forms.Textarea(attrs={
                'class': 'w-[15rem] py-2 px-2',
                'placeholder': 'Say something'
            })
        }
        
class AssignmentsForm(forms.ModelForm):
    class Meta:
        model = Assignments
        fields = ('username', 'courses', 'assignments',)
