from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser, Group

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50, required=True)
    email = forms.EmailField(label='Email', required=False, max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Password again', widget=forms.PasswordInput, required=True)
    #template_name = "form_snippet.html"


class CustomUserChangeForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50, required=True)
    email = forms.EmailField(label='Email', required=False, max_length=50)
    # template_name = "form_snippet.html"


class CustomPasswordChangeForm(forms.Form):
    old_password = forms.CharField(label='Old assword', widget=forms.PasswordInput, required=True)
    password = forms.CharField(label='New password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='New password again', widget=forms.PasswordInput, required=True)
    #template_name = "form_snippet.html"


class CustomGroupCreationForm(forms.Form):
    name = forms.CharField(label='Group name', max_length=50, required=True)
    description = forms.CharField(label='Group description', max_length=200, required=True)
    #template_name = "form_snippet.html"