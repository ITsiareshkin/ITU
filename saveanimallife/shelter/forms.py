from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *

POSITION_CHOICES= [
    ('admin', 'admin'),
    ('vet', 'vet'),
    ('verified', 'verified'),
    ('unverified', 'unverified'),
    ]


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password confirm', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')

KIND_CHOICES = (
    ('Dog', 'Dog'),
    ('Cat', 'Cat')
)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')

)

class AddAnimalForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    kind = forms.ChoiceField(required=True, choices=KIND_CHOICES)
    breed = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    age = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-input'})) # IntegerInput ?
    color = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-input'}))
    gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES)
    discription = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    photo = forms.ImageField(required=True)
    class Meta:
        model = Animal
        fields = ['name', 'kind', 'breed', 'age', 'color', 'gender', 'discription', 'photo']


class EditAnimalForm(forms.ModelForm):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-input'}))
    kind = forms.ChoiceField(required=True, choices=KIND_CHOICES)
    breed = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-input'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-input'}))  # IntegerInput ?
    color = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-input'}))
    gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES)
    discription = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    photo = forms.ImageField()

    class Meta:
        model = Animal
        fields = ['name', 'kind', 'breed', 'age', 'color', 'gender', 'discription', 'photo']


class AdminAddUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Password confirm', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    surname = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'class': 'form-input'}))
    position = forms.CharField(label='Position', widget=forms.Select(choices=POSITION_CHOICES))

    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2', 'name', 'surname', 'position')


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


POSITION_CHOICES = [
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


class CreateWalkForm(forms.ModelForm):
    starting = forms.DateTimeField(label='Beginning time', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    ending = forms.DateTimeField(label='End time', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Walk
        fields = ['starting', 'ending']