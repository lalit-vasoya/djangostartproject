from django import forms
# from .models import ProfileModel,CityModel
from .models import User,CityModel,CleanerModel
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate
from django.core.validators import RegexValidator

phonenumberrexp=RegexValidator(regex='^[0-9]{10}$',message="Enter Valid Mobile Number")


class RegistrationForm(UserCreationForm):
    # phonenumber=forms.CharField(max_length=12,validators=[phonenumberrexp])
    class Meta:
        model=User
        fields=('contact','first_name','last_name','email','password1','password2')
    # city=forms.ModelChoiceField(queryset=CityModel.objects.all(),label="Select City")

   
class LoginForm(forms.Form): 
    contact=forms.CharField(max_length=12,validators=[phonenumberrexp],label="Enter Contact")
    password=forms.CharField(max_length=20,label="Enter Password",widget=forms.PasswordInput())
   
class CleanerForm(forms.ModelForm):
    city=forms.ModelChoiceField(label="Select City",queryset=CityModel.objects.all())
    class Meta:
        model=CleanerModel
        fields=["city"]
