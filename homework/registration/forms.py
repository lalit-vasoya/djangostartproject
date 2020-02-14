from django import forms
# from .models import ProfileModel,CityModel
from .models import User,CityModel,CleanerModel
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
    # phonenumber=forms.CharField(max_length=12,validators=[phonenumberrexp])
    class Meta:
        model=User
        fields=('contact','first_name','last_name','email','password1','password2')
        labels={
            'contact':"Enter Contact",
            'first_name':"Enter First Name",
            'last_name':"Enter Last Name",
            'password1':"Enter Password",
            'password2':"ReEnter Password"   
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control','placeholder':self.fields[field].label})
        del self.fields['contact'].widget.attrs['autofocus']
    # city=forms.ModelChoiceField(queryset=CityModel.objects.all(),label="Select City")

   
class LoginForm(forms.Form): 
    contact=forms.CharField(max_length=10,label="Enter Contact",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Contact'}))
    password=forms.CharField(max_length=20,label="Enter Password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))

   
class CleanerForm(forms.ModelForm):
    city=forms.ModelChoiceField(label="Select City",queryset=CityModel.objects.all())
    class Meta:
        model=CleanerModel
        fields=["city"]
