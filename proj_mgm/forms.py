from django import forms
from .models import Project, User
from django.contrib.auth.forms import AuthenticationForm

class Projectform(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'slug', 'description']

class AuthenticatedUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))






