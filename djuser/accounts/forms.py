from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class RegistrationForm(UserCreationForm):
    city=forms.CharField(max_length=20,label="Enter City")
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2','city')


