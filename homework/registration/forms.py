from django import forms
# from .models import ProfileModel,CityModel
from .models import User
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

    # def clean_phonenumber(self,*args,**kwargs):
    #     num=self.cleaned_data.get('phonenumber')
    #     if ProfileModel.objects.filter(phonenumber=num).exists():
    #         raise forms.ValidationError("Mobile Number Already Exists.")
    #     return num

class LoginForm(forms.Form):
    # username=forms.CharField(max_length=20,label="Enter Username")
    contact=forms.CharField(max_length=12,validators=[phonenumberrexp],label="Enter Contact")
    password=forms.CharField(max_length=20,label="Enter Password",widget=forms.PasswordInput())
    # class Meta:
    #     model=User
    #     fields=['contact','password']
    

