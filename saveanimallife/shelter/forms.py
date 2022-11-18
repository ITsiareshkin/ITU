from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password confirm', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')


class ChangePasswdForm(PasswordChangeForm):
    old_password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label='Password confirm', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class EditProfileForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    surname = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='email', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Account
        fields = ('name', 'surname', 'email')


POSITION_CHOICES= [
    ('admin', 'admin'),
    ('vet', 'vet'),
    ('verified', 'verified'),
    ('unverified', 'unverified'),
    ]


class EditUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    surname = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'class': 'form-input'}))
    position = forms.CharField(label='Position', widget=forms.Select(choices=POSITION_CHOICES))

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'surname', 'position']
