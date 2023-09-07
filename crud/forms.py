from django import forms
from core.models import (
    HTML_CSS,
    JavaScript,
    Python
)

INPUT_CLASSES = """
border-b border-yellow-500 bg-gray-800 xl:w-[18rem] text-yellow-500 focus:bg-gray-800 w-[15rem] p-1
"""


class html_css_form(forms.ModelForm):
    class Meta:
        model = HTML_CSS
        fields = ('title', 'description', 'video',)
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': INPUT_CLASSES
    }))   
    video = forms.CharField(widget=forms.URLInput(attrs={
        'class': INPUT_CLASSES
    }))


class py_form(forms.ModelForm):
    class Meta:
        model = Python
        fields = ('title', 'description', 'video',)
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': INPUT_CLASSES
    }))   
    video = forms.CharField(widget=forms.URLInput(attrs={
        'class': INPUT_CLASSES
    }))

class js_form(forms.ModelForm):
    class Meta:
        model = JavaScript
        fields = ('title', 'description', 'video',)
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASSES
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': INPUT_CLASSES
    }))   
    video = forms.CharField(widget=forms.URLInput(attrs={
        'class': INPUT_CLASSES
    }))
